# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from borrow.models import UserProfile, Event, Product
from django.utils import timezone
from django.shortcuts import redirect, reverse
from django.db.models import ObjectDoesNotExist


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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_loans'] = Event.objects.filter(user=self.request.user)

        return context
    
class ReturnLoanView(LoginRequiredMixin, View):

    def post(self, request):
        redirect_url = reverse('account:profile')

        try:
            loan_id = request.POST.get('loan_id')
            loan = Event.objects.get(id=loan_id, user=request.user)
            loan.return_date = timezone.now()
            loan.save()
        except ObjectDoesNotExist:
            return redirect(redirect_url + '?success=false&event=return')
        
        product = Product.objects.get(id=loan.product.id)
        product.loaned_amount -= 1
        product.save()       
        return redirect(f"{redirect_url}?success=true&event=return")
    