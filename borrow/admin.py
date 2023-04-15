from django.contrib import admin
from .models import Product, Author, Event
from django import forms

class BarInline(admin.TabularInline):
    model = Product.author.through
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    inlines = [
        BarInline,
    ]

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)

class ProductAdmin(admin.ModelAdmin):
    inlines = [BarInline,]

class AdminProduct(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [BarInline,]
    list_display = ('name', 'short_description', 'genre', 'date_added', 'loaned_amount')
    search_fields = ('description', 'name')
    list_filter = ('date_added', 'loaned_amount')

    def short_description(self, obj):
        """Create a shorter version of a description for the Admin interface"""
        CHAR_LIMIT = 60
        if len(obj.description) > CHAR_LIMIT:
            return (obj.description[:CHAR_LIMIT] + '...')
        return obj.description

    short_description.short_description = 'Description'

admin.site.register(Product, AdminProduct)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Event)
