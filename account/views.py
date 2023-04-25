# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from borrow.models import UserProfile, Event
from datetime import datetime, timedelta


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile/user_profile.html'
    context_object_name = 'profile'



    def get_object(self, queryset=None):
        return self.request.user.userprofile


    # spagetit alempaan, jos muutetaan models 
    #   def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user_loans'] = Event.objects.filter(user=self.request.user)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_loans = Event.objects.filter(user=self.request.user)

        user_loans_with_return_dates = []
        for loan in user_loans:
            return_date = loan.loaned_date + timedelta(days=14)
            user_loans_with_return_dates.append((loan, return_date))

        context['user_loans_with_return_dates'] = user_loans_with_return_dates
        return context
        
    