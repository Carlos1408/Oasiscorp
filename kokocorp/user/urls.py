from django.urls import path
from .views import signup
from .views import login
from .views import logout
from .views import profile
from .views import history
from .views import history_detail

urlpatterns = [
    path('', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('history/', history, name='history'),
    path('history_detail/<int:id_order>', history_detail, name='history_detail'),
]
