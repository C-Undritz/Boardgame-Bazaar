"""
Boardgame Bazaar: checkout App - Models
"""


import uuid

from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Order model to record a purchase by any customer
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=0)
    delivery_cost = models.IntegerField(null=False, blank=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    # below two entries added to ensure order record is unique.
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID (string of 32
        characters)
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates the total each time a line item is added.  Determines the
        total quantity of the items bought to calculate discount and then
        use that to calculate the grand total.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        quantity_total = self.lineitems.aggregate(
            Sum('quantity'))['quantity__sum']
        self.delivery_cost = 4

        if quantity_total:
            if quantity_total >= settings.MULTIBUY_DISCOUNT_TWO:
                self.discount = Decimal(self.order_total * Decimal(
                    settings.MULTIBUY_DISCOUNT_TWO / 100))
            elif quantity_total >= settings.MULTIBUY_DISCOUNT_ONE:
                self.discount = Decimal(self.order_total * Decimal(
                    settings.MULTIBUY_DISCOUNT_ONE / 100))
            else:
                self.discount = 0

        self.grand_total = (
            self.order_total - self.discount) + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if it hasn't
        been set already.  From Boutique Ado walkthrough project.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Order line model for each line item of the order.  Stores product, quantity
    and total for each line
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total using
        the line item quantity.  From Boutique Ado walkthrough project.
        """
        if self.product.on_sale:
            self.lineitem_total = self.product.sale_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product ID {self.product.id} on order \
            {self.order.order_number}'
