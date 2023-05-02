from django.contrib import admin
from .models import Product, Author, Event
from django import forms

MAX_PAGE_AMOUNT = 15


class BarInline(admin.TabularInline):
    model = Product.author.through
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'number_of_works')
    search_fields = ('author_name',)
    list_per_page = MAX_PAGE_AMOUNT
    model = Author
    inlines = [
        BarInline,
    ]

    def number_of_works(self, obj):
        return obj.product_set.all().count()


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [BarInline,]
    list_display = ('name', 'short_description', 'genre',
                    'date_added', 'availability', 'is_available')
    search_fields = ('description', 'name')
    list_filter = ('date_added', 'author')
    list_per_page = MAX_PAGE_AMOUNT

    def short_description(self, obj):
        """Create a shorter version of a description for the Admin interface"""
        CHAR_LIMIT = 60
        if len(obj.description) > CHAR_LIMIT:
            return (obj.description[:CHAR_LIMIT] + '...')
        return obj.description

    def is_available(self, obj):
        return bool(obj.amount - obj.loaned_amount)

    def availability(self, obj: Product):
        return f"{obj.loaned_amount}/{obj.amount}"

    # make the availability show up as a checkmark instead of text
    is_available.boolean = True

    short_description.short_description = 'Description'
    is_available.short_description = ''


class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'loaned_date',
                    'last_update', 'return_date', 'actual_return_date', 'is_returned')
    search_fields = ('user__username', 'product__name')
    list_per_page = MAX_PAGE_AMOUNT

    def is_returned(self, obj):
        return bool(obj.actual_return_date)

    is_returned.boolean = True


admin.site.register(Product, ProductAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Event, EventAdmin)
