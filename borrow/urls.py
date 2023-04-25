from django.urls import path

from . import views

app_name = 'borrow'
urlpatterns = [
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('product/<int:pk>/loan/', views.create_loan, name='loan'),
    path('product/<int:pk>/return/', views.return_loan, name='return'),
    path('list', views.ProductListView.as_view(), name='list'),
    path('', views.IndexView.as_view(), name='index'),
]
