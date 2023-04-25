from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, UserProfileView

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
