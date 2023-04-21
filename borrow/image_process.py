from PIL import Image
from django.conf import settings
import os


def save_thumbnail(file_path, file_name) -> str:
    """ save a copy of a given image file and save it to thumbnails folder
    returns the usable path to the thumbnail"""
    thumbnail_folder = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
    # check if thumbnails folder exists, if not, then create one
    if not os.path.exists(thumbnail_folder):
        os.makedirs(thumbnail_folder)

    with Image.open(file_path) as img:
        img.thumbnail((400, 400), Image.ANTIALIAS)
        # thumb_path = os.path.splitext(file_path)[0] + '_thumb.webp'
        filename = os.path.splitext(os.path.basename(file_name))[0]
        copy_filename = f'{filename}.webp'
        copy_path = os.path.join(
            settings.MEDIA_ROOT, 'thumbnails', copy_filename)
        img.save(copy_path, format="webp")
    return os.path.join('/media', 'thumbnails', copy_filename)
