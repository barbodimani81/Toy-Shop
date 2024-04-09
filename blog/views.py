from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Post, Comment, Image, Video
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, ImageSerializer, VideoSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = (
        'id',
        'category',
    )

    search_fields = (
        'title',
        'description',
    )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(is_active=True).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = (
        'id',
        'post',
    )

    search_fields = (
        'title',
        'description',
    )


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.filter(is_active=True).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = (
        'id',
        'post',
    )

    search_fields = (
        'title',
        'image',
    )


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active=True).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = (
        'id',
        'post',
    )

    search_fields = (
        'title',
        'video',
    )
