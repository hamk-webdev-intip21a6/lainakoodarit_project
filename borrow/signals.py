from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Product
from PIL import Image
import os


def convert_to_webp(path_to_image, name):
    image = Image.open(path_to_image)
    filename = os.path.splitext(name)[0]
    copy_filename = f'{filename}.webp'
    copy_path = os.path.join(settings.MEDIA_ROOT, copy_filename)
    image.save(copy_path, format="webp")


@receiver(post_save, sender=Product.image)
def on_save(sender, instance, **kwargs):
    """Only activate this signal when Product's image propery is saved"""
    path = instance.image.path
    name = instance.image.name
    convert_to_webp(path, name)
