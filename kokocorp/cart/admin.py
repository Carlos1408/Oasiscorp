from django.contrib import admin
from .models.order import Order
from .models.order_detail import Order_detail

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'cost', 'user']
    list_filter = ['date']

class Order_detailAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'cost']
    search_fields = ['product']

admin.site.register(Order, OrderAdmin)
admin.site.register(Order_detail, Order_detailAdmin)
