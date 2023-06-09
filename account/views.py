# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView
from borrow.models import UserProfile, Event, Product
from django.utils import timezone
from django.shortcuts import redirect, reverse
from django.db.models import ObjectDoesNotExist
from datetime import datetime, time


class LoggingInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile/user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_loans'] = Event.objects.filter(user=self.request.user)

        context['current_date'] = timezone.now()

        return context


class ReturnLoanView(LoginRequiredMixin, View):

    def post(self, request):
        redirect_url = reverse('account:profile')

        try:
            loan_id = request.POST.get('loan_id')
            loan = Event.objects.get(id=loan_id, user=request.user)
            loan.actual_return_date = timezone.now()
            loan.save()
        except ObjectDoesNotExist:
            return redirect(redirect_url + '?success=false&event=return')

        product = Product.objects.get(id=loan.product.id)
        product.loaned_amount -= 1
        product.save()
        return redirect(f"{redirect_url}?success=true&event=return")
