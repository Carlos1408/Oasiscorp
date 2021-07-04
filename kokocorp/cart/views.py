from django.shortcuts import render, HttpResponse

# Create your views here.
def add_to_cart(request):
    return HttpResponse('add to cart')

def remove_from_cart(request):
    return HttpResponse('remove from cart')

def confirm_order(request):
    return HttpResponse('confirmed order')

def cart(request):
    return HttpResponse('cart')