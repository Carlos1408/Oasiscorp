from django.urls import path
from .views import add
from .views import remove
from .views import confirm
from .views import cart

urlpatterns = [
    path('', cart),
    path('add/', add),
    path('remove/', remove),
    path('confirm/', confirm),
]