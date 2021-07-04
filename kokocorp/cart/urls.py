from django.urls import path
from .views import add_to_cart
from .views import remove_from_cart
from .views import confirm_order
from .views import cart

urlpatterns = [
    path('add-cart/', add_to_cart),
    path('remove-cart/', remove_from_cart),
    path('confirm-order/', confirm_order),
    path('cart/', cart),
]