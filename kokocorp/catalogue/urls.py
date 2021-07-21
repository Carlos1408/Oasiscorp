from django.urls import path
from .views import home
from .views import search
from .views import category
from .views import product

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('category/<int:id_category>', category, name='category'),
    path('product/<int:id_product>', product, name='product'),
]
