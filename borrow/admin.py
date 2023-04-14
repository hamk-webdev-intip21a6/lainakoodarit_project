from django.contrib import admin
from .models import Product
from .models import Product, Author, Event, User

admin.site.register(Product)

admin.site.register(Author)

admin.site.register(User)

admin.site.register(Event)

