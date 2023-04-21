from PIL import Image
from django.conf import settings
import os


def save_thumbnail(file_path, file_name) -> str:
    with Image.open(file_path) as img:
        img.thumbnail((400, 400))
        # thumb_path = os.path.splitext(file_path)[0] + '_thumb.webp'
        filename = os.path.splitext(os.path.basename(file_name))[0]
        copy_filename = f'{filename}.webp'
        copy_path = os.path.join(
            settings.MEDIA_ROOT, 'thumbnails', copy_filename)
        img.save(copy_path, format="webp")
    return os.path.join('media', 'thumbnails', copy_filename)
