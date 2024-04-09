from django.contrib import admin
from django.contrib.admin import register
from .models import Category, Product, Comment, Image, Video


class ProductInLine(admin.StackedInline):
    model = Product
    extra = 1


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'description')

    inlines = (ProductInLine,)


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'category', 'price')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'price', 'category__title', 'category__description')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'description')


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title')
    list_editable = ('is_active', )
    search_fields = ('id', 'title')


@register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title')
    list_editable = ('is_active',)
    search_fields = ('id', 'title')
