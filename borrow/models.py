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
    loaned_amount = models.SmallIntegerField(default=0)
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
    # constants
    LOANED_STATE = "Loaned"
    RETURNED_STATE = "Returned"
    LATE_STATE = "Late"
    # first value is what is set as value and latter is the value that is readable
    # might try subclass enum later, lets try this first
    STATE_CHOICES = [
        (LOANED_STATE, "Loan"),
        (RETURNED_STATE, "Return"),
        (LATE_STATE, "Late"),
    ]

    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=LOANED_STATE,
    )

    # TODO: the same system as in
    user_id = models.SmallIntegerField()
    product_id = models.SmallIntegerField()
    loaned_date = models.DateField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)

    current_time = datetime.datetime.now()
    # updates the value when model is saved
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_update"]

    def __str__(self):
        return f'event: {self.state}, user_id: {self.user_id}, last update: {self.last_update}'
