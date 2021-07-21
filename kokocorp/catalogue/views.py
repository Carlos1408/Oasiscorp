from django.shortcuts import render, HttpResponse, redirect
from .models.category import Category
from .models.product import Product
from ast import literal_eval

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = getContext()
    context['products'] = products
    return render(request, 'catalogue.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        context = getContext()
        context['products'] = Product.objects.filter(name__contains = searched)
    return render(request, 'catalogue.html', context)

def category(request, id_category):
    products = Product.objects.filter(category = id_category)
    context = getContext()
    context['products'] = products
    return render(request, 'catalogue.html', context)

def product(request, id_product):
    print('PRODUCT', id_product, type(id_product))
    product = Product.objects.get(id = id_product)
    product.features = literal_eval(product.features)
    context = getContext()
    context['product'] = product
    return render(request, 'product.html', context)

def getContext():
    categories = Category.objects.all()
    return {
            'categories' : categories,
            'session' : None
            }
