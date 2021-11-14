from django.shortcuts import render, HttpResponse, redirect
from .models.user import User
from cart.models.order import Order
from cart.models.order_detail import Order_detail
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

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
            messages.success(request, 'Sesion iniciada')
        else:
            messages.warning(request, 'Error al iniciar sesion')
    return redirect(prev_url)

def logout(request):
    auth_logout(request)
    messages.success(request, 'Sesion cerrada')
    return redirect('home')

def profile(request):
    context = { 'user' : request.user }
    return render(request, 'user.html', context)

def history(request):
    orders = Order.objects.filter(user = request.user.id)
    context = { 'orders' : orders }
    return render(request, 'history_cart.html', context)

def history_detail(request, id_order):
   order_details = Order_detail.objects.filter(order = id_order)
   context = { 'order_details' : order_details }
   return render(request, 'history_detail.html', context)
