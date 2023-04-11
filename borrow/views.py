# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'borrow/index.html'
    # what name to use in the template for the data returned in get_queryset
    context_object_name = 'listings'

    def get_queryset(self):
        """Return the last five published questions."""

        # return Question.objects.order_by('-pub_date')[:5]
        return [{
            "title": "The Thoughts of Petri - an autobiography",
            "author": "Petri Kuittinen",
            "genre": "Autobiography",
            "thumbnail": "imgs/placeholder-book-1.jpg"
        },
            {
            "title": "Python 101 for JavaScript developers",
            "author": "Dr. Clause Guard",
            "genre": "Education",
            "thumbnail": "imgs/placeholder-book-2.jpg"
        },
            {
            "title": "Epic adventures of a man",
            "author": "Mark Fischbac",
            "genre": "Fantasy",
            "thumbnail": "imgs/placeholder-book-3.jpg"
        },
            {
            "title": "To ; or not to ;",
            "author": "reddit.com",
            "genre": "Humor",
            "thumbnail": "imgs/placeholder-book-4.jpg"
        },
            {
            "title": "How do I center a div?",
            "author": "sakuk",
            "genre": "Documentation",
            "thumbnail": "imgs/placeholder-book-5.jpg"
        }]


# TODO: change to inherit detailview instead of listview
class ProductView(generic.ListView):
    template_name = 'borrow/product_page.html'
    # TODO: change this to a database object when database is ready
    # model = Product
    context_object_name = 'product'

    def get_queryset(self):
        """Return the clicked on product"""
        return [{
            "title": "How do I center a div?",
            "author": "sakuk",
            "genre": "Documentation",
            "thumbnail": "imgs/placeholder-book-5.jpg",
            "category": "book",
            "description": "'How to Center a Div' is a comprehensive guide for \
            web developers and designers seeking to perfect the art of centering \
            div elements on a webpage. This book offers clear and concise explanations \
            of different techniques for achieving perfect div centering, including CSS \
            properties such as margin, padding, display, and position. Additionally, \
            readers will learn how to use different types of layouts, such as flexbox \
            and grid, to create responsive and dynamic centering solutions."
        }]
