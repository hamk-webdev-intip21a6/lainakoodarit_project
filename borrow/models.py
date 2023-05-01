from django.db import models
import datetime
from .image_process import save_thumbnail
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you'd like for the user profile

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    home_country = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ["author_name"]

    def __str__(self):
        return self.author_name


class Product(models.Model):
    # NON NULLABLE values - must be filled
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    description = models.TextField(
        max_length=750, default="description not available")
    date_added = models.DateField(auto_now_add=True)
    author = models.ManyToManyField(Author)
    category = models.CharField(max_length=30)
    amount = models.SmallIntegerField(default=0)
    loaned_amount = models.SmallIntegerField(default=0, editable=False)
    # NULLABLE fields - can be left empty
    genre = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    # we could use a randomly chosen thumbnail for if there is no image provided
    image = models.ImageField(
        upload_to="images/", blank=True, null=True)
    thumbnail = models.CharField(
        max_length=75, blank=True, null=True, editable=False)
    # purchase_event

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Save a thumbail for the product that is smaller and faster to load"""
        super().save(*args, **kwargs)
        if self.image:
            thumb_path = save_thumbnail(self.image.path, self.image.name)
            self.thumbnail = thumb_path
            super().save(*args, **kwargs)


class Event(models.Model):
    # TODO: the same system as in
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, default=None)
    loaned_date = models.DateField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True, editable=False)
    actual_return_date = models.DateTimeField(blank=True, null=True, editable=False)
    # updates the value when model is saved
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-last_update"]

    def __str__(self):
        return f'event: user_id: {self.user}, last update: {self.last_update}'
