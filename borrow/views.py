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
            "title": "the thoughts of Petri - an autobiography",
            "author": "Petri Kuittinen",
            "genre": "Autobiography",
            "thumbnail": "imgs/placeholder-book-1.jpg"
        },
            {
            "title": "Python 101 for javascript developers",
            "author": "Some Dude",
            "genre": "Documentation",
            "thumbnail": "imgs/placeholder-book-2.jpg"
        },
            {
            "title": "Epic adventures of a man",
            "author": "Mark Fischbac",
            "genre": "Fantasy",
            "thumbnail": "imgs/placeholder-book-3.jpg"
        },
            {
            "title": "Databases are overrated",
            "author": "reddit.com",
            "genre": "Humor",
            "thumbnail": "imgs/placeholder-book-4.jpg"
        },
            {
            "title": "Testing testing",
            "author": "Some Dude",
            "genre": "Documentation",
            "thumbnail": "imgs/placeholder-book-5.jpg"
        }]
