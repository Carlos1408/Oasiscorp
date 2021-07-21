from django.shortcuts import render, redirect, HttpResponse
from catalogue.models.product import Product
from catalogue.models.category import Category
from .cart import Cart
# Create your views here.
def cart(request):
    context = {
            'categories' : Category.objects.all(),
            'session' : None
            }
    return render(request, 'cart.html', context)

def add(request, id_product):
    product = Product.objects.get(id = id_product)
    prev_url = request.META.get('HTTP_REFERER')
    cart = Cart(request)
    if request.method == 'GET':
        cart.addProduct(product)
        print('Add 1')
    elif request.method == 'POST':
        quantity = request.POST['quantity']
        cart.addProduct(product, int(quantity))
        print('Add ', quantity)
    print(cart.cart)
    print(cart.total)
    return redirect(prev_url)

def remove(request, id_product):
    print(id_product, type(id_product))
    cart = Cart(request)
    cart.removeProduct(id_product)
    return redirect('cart')

def confirm(request):
    cart = Cart(request)
    if request.user.is_authenticated:
       if cart.cart:
            cart.confirmOrder(request)
    else:
        print('user not authenticated')
        return redirect('cart')
    return redirect('home')
