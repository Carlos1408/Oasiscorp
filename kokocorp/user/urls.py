from django.urls import path
from .views import signup
from .views import login
from .views import logout
from .views import my_profile
from .views import history

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('my-profile/', my_profile),
    path('history/', history),
]