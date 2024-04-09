from django.contrib import admin
from django.contrib.admin import register
from .models import Category, Post, Comment, Image, Video


class PostInLine(admin.StackedInline):
    model = Post
    extra = 1


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'description')

    inlines = (PostInLine,)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'category')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'description', 'category__title', 'category__description')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'post')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'description', 'post__title', 'post__description')


@register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post', 'image', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title', 'post')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'post')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'post__title')


@register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post', 'video', 'is_active', 'created_date', 'updated_date')
    list_display_links = ('id', 'title', 'post')
    list_filter = ('is_active', 'created_date', 'updated_date', 'title', 'post')
    list_editable = ('is_active',)
    search_fields = ('id', 'title', 'post__title')
