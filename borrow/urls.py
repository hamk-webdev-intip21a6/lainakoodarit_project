from django.urls import path

from . import views

app_name = 'borrow'  # namespace for urls
urlpatterns = [
    # product page
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),
    # the loaning view for the product
    path('product/<int:pk>/loan/', views.create_loan, name='loan'),
    # the return view for the product
    path('product/<int:pk>/return/', views.return_loan, name='return'),
    # the list view for all of the products
    path('list', views.ProductListView.as_view(), name='list'),
    # use the index page as root for the borrow application
    path('', views.IndexView.as_view(), name='index'),
]
