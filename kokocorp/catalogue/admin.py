from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.supplier import Supplier

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'unit_price', 'category']
    list_editable = ['stock',]
    search_fields = ['name',]
    list_filter = ['category', 'supplier']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
