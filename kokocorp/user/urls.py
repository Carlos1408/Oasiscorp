from django.urls import path
from .views import signup
from .views import login
from .views import logout
from .views import user
from .views import history

urlpatterns = [
    path('', user),
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('history/', history),
]