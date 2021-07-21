# from django.test import TestCase

# Create your tests here.

from cart import Cart

cart1 = Cart('Carrito1')
cart2 = Cart('Carrito2')

print(cart1.getMessage())
print(cart2.getMessage())
