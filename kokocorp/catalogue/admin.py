from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.supplier import Supplier

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)