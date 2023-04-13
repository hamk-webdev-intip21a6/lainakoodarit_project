from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
    # NON NULLABLE values - must be filled
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    amount = models.SmallIntegerField(default=0)
    descrtiption = models.CharField(max_length=250)
    release_date = models.DateField(default=datetime.date.today)
    loaned_amount = models.SmallIntegerField(default=0)
    # author = models.ManyToManyField(author)
    # NULLABLE fields - can be left empty
    genre = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    # we could use a randomly chosen thumbnail for if there is no image provided
    thumbnail_path = models.CharField(max_length=50)
    # category
    # purchase_event

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
