from django.shortcuts import render, HttpResponse, redirect
from .models.user import User
from cart.models.order import Order
from cart.models.order_detail import Order_detail
from catalogue.models.category import Category
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    context = {
            'categories' : Category.objects.all()
            }
    if request.method == 'GET':
        return render(request, 'signup.html', context)

    elif request.method == 'POST':
        f = request.POST
        if f['password'] == f['c_password']:
            user = User.objects.create_user(
                    first_name = f['first_name'],
                    last_name = f['last_name'],
                    birth_date = f['birth_date'],
                    phone = f['phone'],
                    address = f['address'],
                    email = f['email'],
                    password = f['password']
                    )
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('signup')

def login(request):
    if request.method == 'POST':
        prev_url = request.META.get('HTTP_REFERER')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            print('LOGUEADO')
        else:
            print('NO LOGUEADO')
    return redirect(prev_url)

def logout(request):
    auth_logout(request)
    return redirect('home')

def profile(request):
    context = {
            'categories' : Category.objects.all(),
            'user' : request.user
            }
    return render(request, 'user.html', context)

def history(request):
    orders = Order.objects.filter(user = request.user.id)
    print(orders)
    context = {
            'categories' : Category.objects.all(),
            'orders' : orders
            }
    return render(request, 'history_cart.html', context)

def history_detail(request, id_order):
   order_details = Order_detail.objects.filter(order = id_order)
   print(order_details)
   context = {
           'categories' : Category.objects.all(),
           'order_details' : order_details
           }
   return render(request, 'history_detail.html', context)
