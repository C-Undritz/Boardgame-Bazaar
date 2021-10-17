from django.db import models
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

import datetime


class CustomManager(models.Manager):

    def determine_new_or_preorder(self, products):
        """
        Determines whether product is a new release or pre-order by running
        queries against the recorded product release_date and the present
        date and updates the product boolean values accordingly.
        """
        new_release_time_period = 90
        today = datetime.date.today()
        delta = datetime.timedelta(days=new_release_time_period)
        past_date = today - delta

        for product in products:
            if (product.release_date > past_date) and (product.release_date < today):
                this_product = product
                this_product.new_release = True
                this_product.save()
            else:
                this_product = product
                this_product.new_release = False
                this_product.save()
            if product.release_date > today:
                this_product = product
                this_product.pre_order = True
                this_product.save()
            else:
                this_product = product
                this_product.pre_order = False
                this_product.save()
        return products

    def all(self):
        products = super().all()
        products = self.determine_new_or_preorder(products)
        return products


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    genre = models.ManyToManyField(Genre, through="GenreAssignment")
    stock = models.IntegerField(null=False, blank=False, default=0)
    sold = models.IntegerField(null=False, blank=False, default=0)
    image = models.ImageField(null=True, blank=True)
    pre_order = models.BooleanField(default=False)
    new_release = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=False, default=0)

    objects = CustomManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Product, self).save(*args, **kwargs)
        
    def update_stock_sold(self, instance):
        """
        Uses the sold quantities of products into to update the stock and sold
        figures.
        """
        self.stock = self.stock - instance.quantity
        self.sold = self.sold + instance.quantity
        self.save()

    def update_rating(self, instance):
        """
        Determines each products average rating from all user ratings for that
        product.
        """
        self.rating = self.reviews.all().aggregate(Avg('rating'))['rating__avg']
        self.save()


class GenreAssignment(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['genre', 'product']]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
