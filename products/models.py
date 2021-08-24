from django.db import models


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
    genre = models.ManyToManyField(Genre, through="GenreAssignment")
    stock = models.IntegerField(null=False, blank=False, default=0)
    sold = models.IntegerField(null=False, blank=False, default=0)
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=CATEGORY_DEFAULT)
    condition = models.ForeignKey('Condition', on_delete=models.SET_DEFAULT, default=CONDITION_DEFAULT)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class GenreAssignment(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['genre', 'Product']]
