from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
from .models import Product


def remove_images(image_path: str) -> None:
    """Remove the old product images"""
    try:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        thumbnail_path = os.path.join(
            settings.MEDIA_ROOT, 'thumbnails', f"{image_name}.webp")
        # remove the thumbnail
        os.remove(thumbnail_path)
        # and the full image
        os.remove(image_path)
    except OSError as error:
        print('OSError:', error)
    return


@receiver(pre_save, sender=Product)
def on_save(sender, instance, **kwargs) -> None:
    """If new Product.image is different from the previous
    remove the old product images"""
    try:
        # get the old object and it's path
        old_object = Product.objects.filter(pk=instance.pk).first()
        old_image_path = old_object.image.path
        # check that the instance's image has changed
        instance.image.path
    except OSError as error:
        return print("OSError:", error)
    except:
        return
    # check if the image path has been changed
    if old_image_path == instance.image.path:
        return
    remove_images(old_image_path)


@receiver(pre_delete, sender=Product)
def on_delete(sender, instance, **kwargs) -> None:
    """Delete the thumbnail and image of a file when product is removed"""
    remove_images(instance)
