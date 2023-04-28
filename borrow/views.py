# Create your views here.
from django.db.models import ObjectDoesNotExist
from django.views import generic
from .models import Product, Event
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'borrow/index.html'
    # what name to use in the template for the data returned in get_queryset
    context_object_name = 'listings'

    def get_queryset(self):
        """ Return the five most recent objects in the product category """
        return Product.objects.order_by('-date_added')


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

        user = self.request.user
        if not user:
            return context
        user_loan = Event.objects.filter(
            user=user.id, product=product.id, return_date__isnull=True)
        context['user_loaned'] = user_loan.exists()
        return context


class ProductListView(generic.ListView):
    """View for the product list page."""
    template_name = 'borrow/product_list.html'
    context_object_name = 'listings'
    ordering = '-date_added'
    model = Product

    def get_queryset(self):
        """Check if the template passed a GET query.
        If so, use the keyword variable's value to filter the database query.

        - this is created in a way that you don't have to manually type every
        case for a filter. This function loops through all Product fields and
        checks for filters programatically
        """
        queryset = super().get_queryset()
        # loops through the GET requests
        for key, values in self.request.GET.lists():
            # check if the key agument of a request is a Product attribute
            print(key, values)
            if not hasattr(Product, key):
                # if not, keep iterating
                continue
            # check that the request is not empty
            if values[0] is "":
                continue
            # if prior checks have passed, loop through the values
            # and use them as filters for the database query
            for value in values:
                queryset = queryset.filter(**{f"{key}__icontains": value})
        # return the queryset and order by the given ordering
        return queryset.order_by(self.ordering)


@login_required
def create_loan(request, pk):
    # first get the product
    product = get_object_or_404(Product, pk=pk)
    redirect_url = reverse_lazy('borrow:product', kwargs={'pk': product.pk})
    try:
        # then create a loan event
        loan = Event.objects.create(user=request.user, product=product)
        loan.save()
    except ObjectDoesNotExist:
        return redirect(redirect_url + '?success=false&event=loan')
    # when everything is done successfully, add the loan to the loaned amount
    product.loaned_amount += 1
    product.save()
    # redirect the user back to the product page afterwards
    return redirect(redirect_url + '?success=true&event=loan')


@login_required
def return_loan(request, pk):
    # first get the product
    product = get_object_or_404(Product, pk=pk)
    redirect_url = reverse_lazy('borrow:product', kwargs={'pk': product.pk})
    try:
        # then update the loaned event to have a return date
        loan = Event.objects.get(
            user=request.user, product=product, return_date__isnull=True)
        loan.return_date = timezone.now()
        loan.save()
    except ObjectDoesNotExist:
        return redirect(redirect_url + '?success=false&event=return')
    # when everything is done successfully, remove the loan from the loaned_amount
    product.loaned_amount -= 1
    product.save()
    # redirect the user back to the product page afterwards
    return redirect(redirect_url + '?success=true&event=return')
