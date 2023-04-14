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


# TODO: change to inherit detailview instead of listview
# when the models for the product are up and running
class ProductView(generic.ListView):
    template_name = 'borrow/product_page.html'
    # TODO: change this to a database object when database is ready
    model = Product
    context_object_name = 'product'

    def get_queryset(self):
        """Return the clicked on product"""
        return [{
            "title": "How do I center a div?",
            "author": "sakuk",
            "genre": "Documentation",
            "thumbnail": "imgs/placeholder-book-5.jpg",
            "category": "Book",
            "tags": ["cool", "epic", "thought-provoking"],
            "date_added": "12.2.2023",
            "language": "English",
            "availability": f"{5}/{7}",
            "description": "'How to Center a Div' is a comprehensive guide for \
            web developers and designers seeking to perfect the art of centering \
            div elements on a webpage. This book offers clear and concise explanations \
            of different techniques for achieving perfect div centering, including CSS"
        }]


class ProductListView(generic.ListView):
    template_name = 'borrow/product_list.html'
    context_object_name = 'listings'
    model = Product
    queryset = Product.objects.order_by('-release_date')
