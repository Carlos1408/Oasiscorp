from django.contrib import admin
from .models.order import Order
from .models.order_detail import Order_detail

# Register your models here.

admin.site.register(Order)
admin.site.register(Order_detail)