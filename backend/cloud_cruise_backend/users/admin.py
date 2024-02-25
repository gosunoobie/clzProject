from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email','is_staff','is_superuser')
