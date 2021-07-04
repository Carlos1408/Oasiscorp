from django.shortcuts import render, HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse('signup')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def my_profile(request):
    return HttpResponse('my profile')

def history(request):
    return HttpResponse('history')

