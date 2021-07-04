from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')

def products(request):
    return HttpResponse('view all')

def category(request):
    return HttpResponse('category')

def product(request):
    return HttpResponse('product')