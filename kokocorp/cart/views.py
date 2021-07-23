from django.shortcuts import render, redirect, HttpResponse
from catalogue.models.product import Product
from .cart import Cart
from django.contrib import messages
# Create your views here.
def cart(request):
    return render(request, 'cart.html')

def add(request, id_product):
    product = Product.objects.get(id = id_product)
    prev_url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    if request.method == 'GET':
        cart.addProduct(product)
    elif request.method == 'POST':
        quantity = request.POST['quantity']
        cart.addProduct(product, int(quantity))
    messages.success(request, f'{product.name} agregado al carrito')
    return redirect(prev_url)

def remove(request, id_product):
    cart = Cart(request)
    cart.removeProduct(id_product)
    messages.warning(request, 'Producto removido del carrito')
    return redirect('cart')

def confirm(request):
    cart = Cart(request)
    if request.user.is_authenticated:
       if cart.cart:
            messages.success(request, 'Pedido realizado exitosamente')
            cart.confirmOrder(request)
       else:
            messages.warning(request, 'Carrito vacio')
    else:
        messages.warning(request, 'Debe iniciar sesion')
        return redirect('cart')
    return redirect('home')
