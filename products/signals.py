from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when lineitem updated/created
    """
    instance.product.update_rating(instance)
