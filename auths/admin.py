from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = [
        'username','email',
        'phone','age'
    ]

    list_display_links = ['username']

    list_per_page = 120

    list_max_show_all = 120

    