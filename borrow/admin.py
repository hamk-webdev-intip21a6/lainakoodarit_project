from django.contrib import admin
from .models import Product, Author, Event, User


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'genre',
                    'date_added', 'loaned_amount')
    search_fields = ('description', 'name')
    list_filter = ('date_added', 'loaned_amount')

    def short_description(self, obj):
        """Create a shorter version of a description for the
        Admin interface"""
        CHAR_LIMIT = 60
        if len(obj.description) > CHAR_LIMIT:
            return (obj.description[:CHAR_LIMIT] + '...')
        return obj.description

    short_description.short_description = 'Description'


admin.site.register(Product, AdminProduct)

admin.site.register(Author)

admin.site.register(User)

admin.site.register(Event)
