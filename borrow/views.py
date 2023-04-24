# Create your views here.
from django.views import generic
from .models import Product, Event
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'borrow/index.html'
    # what name to use in the template for the data returned in get_queryset
    context_object_name = 'listings'

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
        return context


class ProductListView(generic.ListView):
    """View for the product list page."""
    template_name = 'borrow/product_list.html'
    context_object_name = 'listings'
    model = Product

    def get_queryset(self):
        """Check if the template passed a GET query.
        If so, use the keyword variable's value to filter the database query"""
        queryset = Product.objects
        # if a get request is NOT included in the url, return all of the objects
        if not self.request.GET:
            return queryset.order_by('-date_added')
        # if a get request is included, here is what to do with it
        category_filter = self.request.GET['category']
        if category_filter:
            queryset = queryset.filter(category=category_filter)
        # at the end, return the queryset with the filters added
        return queryset.order_by('-date_added')


@login_required
def create_loan(request, pk):
    product = get_object_or_404(Product, pk=pk)
    event = Event.objects.create(user=request.user, product=product)
    event.save()
    # others
    return redirect('borrow:product', pk=product.pk)
