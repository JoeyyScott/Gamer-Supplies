# Imports
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CrateItems


@receiver(post_save, sender=CrateItems)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when items are added to or updated in the crate
    """
    instance.order.update_total()


@receiver(post_delete, sender=CrateItems)
def update_on_delete(sender, instance, created, **kwargs):
    """
    Update order total when items are deleted from the crate
    """
    instance.order.update_total()
