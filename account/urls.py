from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, UserProfileView, ReturnLoanView

app_name = 'account'
urlpatterns = [
    path('return_loan/', ReturnLoanView.as_view(), name='return_loan'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
