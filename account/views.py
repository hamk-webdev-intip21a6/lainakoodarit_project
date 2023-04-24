from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from borrow.models import UserProfile


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