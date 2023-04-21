from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product


# @receiver(post_save, sender=Product)
# def on_save(sender, instance, created, **kwargs) -> None:
#     """Only activate this signal when Product's image propery is saved"""
#     if not created:
#         return

@receiver(post_delete, sender=Product)
def on_delete(sender, instance, **kwargs) -> None:
    """Delete the files that we're used for the deleted image"""
    return
