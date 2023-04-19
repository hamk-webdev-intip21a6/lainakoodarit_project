# Create your views here.
from django.views import generic
from .models import Product
from random import randint


def random_default_thumbnail(category: str) -> str:
    """Get a random image for a product, if product doesn't have one already.
    @param context, is_list"""
    # if context for DetailView is wanted
    random_num = randint(1, 5)
    return f"defaults/placeholder-{category}-{random_num}.jpg"


class IndexView(generic.ListView):
    template_name = 'borrow/index.html'
    # what name to use in the template for the data returned in get_queryset
    context_object_name = 'listings'

    def get_context_data(self, **kwargs):
        # get the context
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            if not obj.image:
                obj.image = random_default_thumbnail(obj.category)
        return context

    def get_queryset(self):
        """ Return the five most recent objects in the product category """
        return Product.objects.order_by('-date_added')[:5]


class ProductView(generic.DetailView):
    # TODO: change this to a database object when database is ready
    model = Product
    context_object_name = 'product'
    template_name = 'borrow/product_page.html'

    def get_context_data(self, **kwargs):
        """Calculate the amount of copies available and add to the view context"""
        context = super().get_context_data(**kwargs)
        # get a default image for product, if image does not exist
        if not context['object'].image:
            context['object'].image = random_default_thumbnail(
                context['object'].category)
        product = self.get_object()
        # calculate the amount of available copies
        available = product.amount - product.loaned_amount
        # add the value to be available in the context
        # use {{ available }} to use it
        context['available'] = available
        # also add a list of 5 most recent products of the same category
        current_category = context['object'].category
        context['recent_additions'] = Product.objects.filter(
            category=current_category)[:5]
        for obj in context['recent_additions']:
            if not obj.image:
                obj.image = random_default_thumbnail(obj.category)
        return context


class ProductListView(generic.ListView):
    template_name = 'borrow/product_list.html'
    context_object_name = 'listings'
    model = Product

    def get_context_data(self, **kwargs):
        # get the context
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            if not obj.image:
                obj.image = random_default_thumbnail(obj.category)
        return context

    def get_queryset(self):
        """Check if the template passed a GET query.
        If so, use the keyword variable's value to filter the database query"""
        queryset = Product.objects
        category_filter = self.request.GET['category']
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        return queryset.order_by('-date_added')
