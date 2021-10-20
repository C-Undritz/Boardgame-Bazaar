"""
Boardgame Bazaar: profile App - Models
"""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from products.models import Product


class UserProfile(models.Model):
    """
    User profile for the storage of delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Delivery Address and contact details
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    # Customers wishlist
    wishlist = models.ManyToManyField(
        Product, related_name='wishlist', default=None, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver for the post save event from the user model. Creates a
    profile if user has been created or saves profile to update it if user
    already exists.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
