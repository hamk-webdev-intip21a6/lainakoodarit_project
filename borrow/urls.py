from django.urls import path

from . import views

app_name = 'borrow'
urlpatterns = [
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('list', views.ProductListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name='index'),
]
