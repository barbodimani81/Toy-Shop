from django.contrib import admin
from django.contrib.admin import register

from .models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'created_date', 'updated_date', 'username')
    list_editable = ('is_active',)
    search_fields = ('id', 'username')

