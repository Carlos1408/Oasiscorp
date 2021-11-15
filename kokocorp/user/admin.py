from django.contrib import admin
from .models.user import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'admin', 'active']
    list_editable = ['admin',]
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['admin', 'active']

admin.site.register(User, UserAdmin)
