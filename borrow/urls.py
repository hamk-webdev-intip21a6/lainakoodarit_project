from django.urls import path

from . import views

app_name = 'borrow'
urlpatterns = [
    path('product', views.ProductView.as_view(), name='product'),
    path('', views.IndexView.as_view(), name='index'),
]
