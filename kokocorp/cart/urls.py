from django.urls import path
from .views import add
from .views import remove
from .views import confirm
from .views import cart

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:id_product>', add, name='add'),
    path('remove/<id_product>', remove, name='remove'),
    path('confirm/', confirm, name='confirm'),
]
