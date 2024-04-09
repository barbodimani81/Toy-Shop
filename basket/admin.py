from django.contrib import admin
from django.contrib.admin import register

from .models import Basket


@register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('title', )
    search_fields = ('title', )
