from django.urls import path
from .views import *

urlpatterns = [
  path('products/', ProductLCView.as_view(), name='products-list-create'),
  path('products/<int:pk>/', ProductRUDView.as_view(), name='product-detail'),
  # path('orderbyprice/', OrderByPrice.as_view(), name='order-by-price'),
]