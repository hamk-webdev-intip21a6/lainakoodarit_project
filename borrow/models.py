from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    # NON NULLABLE values - must be filled
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    descrtiption = models.CharField(max_length=250)
    thumbnail_path = models.CharField(max_length=50)
    amount = models.SmallIntegerField(default=0)
    release_date = models.DateField(default=datetime.date.today)
    loaned_amount = models.SmallIntegerField(default=0)
    # author = models.ManyToManyField(author)
    # NULLABLE fields - can be left empty
    genre = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    # category
    # purchase_event

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
