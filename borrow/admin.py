from django.contrib import admin
from .models import Product, Author, Event
from django import forms

# amount of items to show per page in the admin interface
MAX_PAGE_AMOUNT = 15


class BarInline(admin.TabularInline):
    model = Product.author.through
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    """Author model's admin page configuration"""
    list_display = ('author_name', 'number_of_works')
    search_fields = ('author_name',)
    model = Author
    inlines = [
        BarInline,
    ]
    # pagination
    list_per_page = MAX_PAGE_AMOUNT

    def number_of_works(self, obj):
        return obj.product_set.all().count()


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('author',)


class ProductAdmin(admin.ModelAdmin):
    """Product model's admin page configuration"""
    form = ProductAdminForm
    inlines = [BarInline,]
    list_display = ('name', 'short_description', 'genre',
                    'date_added', 'availability', 'is_available')
    search_fields = ('description', 'name')
    list_filter = ('date_added', 'author')
    # pagination
    list_per_page = MAX_PAGE_AMOUNT

    def short_description(self, obj):
        """Create a shorter version of a description for the Admin interface"""
        CHAR_LIMIT = 60
        if len(obj.description) > CHAR_LIMIT:
            return (obj.description[:CHAR_LIMIT] + '...')
        return obj.description

    def is_available(self, obj):
        """Calculate if there are available copies, return result as boolean"""
        return obj.amount > obj.loaned_amount

    def availability(self, obj: Product):
        """Create a string in the format of loaned_amount/amount_in_storage"""
        return f"{obj.loaned_amount}/{obj.amount}"

    # make the availability show up as a checkmark instead of text
    is_available.boolean = True

    # change the headers for the following columns
    short_description.short_description = 'Description'
    is_available.short_description = ''


class EventAdmin(admin.ModelAdmin):
    """Product model's admin page configuration"""
    list_display = ('user', 'product', 'loaned_date',
                    'last_update', 'return_date', 'actual_return_date', 'is_returned')
    search_fields = ('user__username', 'product__name')
    # pagination
    list_per_page = MAX_PAGE_AMOUNT

    def is_returned(self, obj):
        """Check if product is already returned based on if actual_return_date is null or not"""
        return bool(obj.actual_return_date)

    is_returned.boolean = True


# actually register the Models and their interfaces to Admin page
admin.site.register(Product, ProductAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Event, EventAdmin)
