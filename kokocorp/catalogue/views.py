from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')

def view_all(request):
    return HttpResponse('view all')

def view_category(request):
    return HttpResponse('category')

def view_product(request):
    return HttpResponse('product')