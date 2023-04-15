from django.contrib import admin
from .models import Product, Author, Event
from django import forms


class BarInline(admin.TabularInline):
    model = Product.author.through
    extra = 0 
    

class AuthorAdmin(admin.ModelAdmin):
    model = Product
    inlines = [
            BarInline,
            ]
    
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [BarInline,]

admin.site.register(Product, ProductAdmin)

admin.site.register(Author, AuthorAdmin)


admin.site.register(Event)

