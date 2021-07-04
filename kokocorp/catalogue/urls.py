from django.urls import path
from .views import home
from .views import products
from .views import category
from .views import product

urlpatterns = [
    path('', home),
    path('products/', products),
    path('category/', category),
    path('product/', product),
]