from django.db.models.fields.files import default_storage
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Product


@receiver(pre_save, sender=Product)
def on_save(sender, instance, **kwargs) -> None:
    """If new Product.image is different from the previous
    remove the old product images"""
    if not instance.pk and not instance.image:
        return
    # get the old object and check if the product already exists
    old_object = Product.objects.filter(pk=instance.pk).first()
    if not old_object:
        return
    old_image_path = old_object.image.path
    # check if the image path has been changed
    if old_image_path == instance.image.path:
        return
    try:
        image_name = os.path.splitext(os.path.basename(old_image_path))[0]
        thumbnail_path = os.path.join(
            settings.MEDIA_ROOT, 'thumbnails', f"{image_name}.webp")
        # remove the old thumbnail
        os.remove(thumbnail_path)
        # remove the old full image
        os.remove(old_image_path)
    except OSError as error:
        print('OSERROR:', error)


@receiver(pre_delete, sender=Product)
def on_delete(sender, instance, **kwargs) -> None:
    """Delete the thumbnail and image of a file when product is removed"""
    try:
        image_name = os.path.splitext(os.path.basename(instance.image.path))[0]
        thumbnail_path = os.path.join(
            settings.MEDIA_ROOT, 'thumbnails', f"{image_name}.webp")
        # remove the thumbnail
        os.remove(thumbnail_path)
        # and the full image
        os.remove(instance.image.path)
    except:
        pass
    return
