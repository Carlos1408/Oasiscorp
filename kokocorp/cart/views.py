from django.shortcuts import render, HttpResponse

# Create your views here.
def cart(request):
    return HttpResponse('cart')

def add(request):
    return HttpResponse('add to cart')

def remove(request):
    return HttpResponse('remove from cart')

def confirm(request):
    return HttpResponse('confirmed order')