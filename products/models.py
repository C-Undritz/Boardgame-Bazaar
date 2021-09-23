from django.db import models
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User


CATEGORY_DEFAULT = 'none'
CONDITION_DEFAULT = 'undetermined'


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Condition(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    description = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    genre = models.ManyToManyField(Genre, through="GenreAssignment")
    stock = models.IntegerField(null=False, blank=False, default=0)
    sold = models.IntegerField(null=False, blank=False, default=0)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=CATEGORY_DEFAULT)
    condition = models.ForeignKey('Condition', on_delete=models.SET_DEFAULT, default=CONDITION_DEFAULT)
    image = models.ImageField(null=True, blank=True)
    # Category fields rendered as boolean to try out queries
    used = models.BooleanField(default=False)
    pre_order = models.BooleanField(default=False)
    new_release = models.BooleanField(default=False)
    current_rating = models.IntegerField(null=False, blank=False, default=0)
    ratings_total = models.IntegerField(null=False, blank=False, default=0)
    ratings_number = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.product_name

    def update_stock_sold(self, instance):
        product = get_object_or_404(Product, pk=instance.product_id)
        product.stock = product.stock - instance.quantity
        product.sold = product.sold + instance.quantity
        product.save()
    
    def update_rating(self, instance):
        product = get_object_or_404(Product, pk=instance.product_id)
        product.ratings_total = product.ratings_total + instance.rating
        product.ratings_number += 1
        product.current_rating = product.ratings_total // product.ratings_number
        product.save()


class GenreAssignment(models.Model):
    # genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['genre', 'product']]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField(max_length=500, blank=False)
    rating = models.IntegerField(null=False, blank=False, default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
