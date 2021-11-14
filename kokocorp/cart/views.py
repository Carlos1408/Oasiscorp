from django.shortcuts import render, redirect, HttpResponse
from catalogue.models.product import Product
from .cart import Cart
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

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
            # ENVIO DE EMAIL
            ## RENDERIZADO DE CORREO
            context = {'cart' : cart.cart, 'total' : cart.total}
            template = get_template('mail.html')
            content = template.render(context)
            email = EmailMultiAlternatives(
                    'Recibo de compra',
                    'Compra realizada',
                    settings.EMAIL_HOST_USER,
                    [request.user.email]
                    )
            email.attach_alternative(content, 'text/html')
            email.send()

            cart.confirmOrder(request)
       else:
            messages.warning(request, 'Carrito vacio')
    else:
        messages.warning(request, 'Debe iniciar sesion')
        return redirect('cart')
    return redirect('home')
