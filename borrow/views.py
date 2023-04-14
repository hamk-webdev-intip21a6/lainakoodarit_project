# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Product


class IndexView(generic.ListView):
    template_name = 'borrow/index.html'
    # what name to use in the template for the data returned in get_queryset
    context_object_name = 'listings'

    def get_queryset(self):
        """ Return the five most recent objects in the product category """
        # for example     v
        return Product.objects.order_by('-release_date')[:5]


class ProductView(generic.DetailView):
    # TODO: change this to a database object when database is ready
    model = Product
    context_object_name = 'product'
    template_name = 'borrow/product_page.html'

    def get_context_data(self, **kwargs):
        """Calculate the amount of copies available and add to the view context"""
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        # calculate the amount of available copies
        available = product.amount - product.loaned_amount
        # add the value to be available in the context
        # use {{ available }} to use it
        context['available'] = available
        # context['available'] = 0
        return context


class ProductListView(generic.ListView):
    template_name = 'borrow/product_list.html'
    context_object_name = 'listings'
    model = Product
    queryset = Product.objects.order_by('-release_date')
