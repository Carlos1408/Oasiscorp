from django.urls import path
from .views import view_all
from .views import view_category
from .views import view_product
from .views import home

urlpatterns = [
    path('', home),
    path('view-all/', view_all),
    path('view-category/', view_category),
    path('view-product/', view_product),
]