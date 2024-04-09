from rest_framework import serializers

from .models import Category, Post, Comment, Image, Video


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'is_active',
            'description',
            'created_date',
            'updated_date',
        )


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = (
            'title',
            'is_active',
            'description',
            'category',
            'created_date',
            'updated_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = (
            'title',
            'is_active',
            'description',
            'post',
            'created_date',
            'updated_date',
        )


class ImageSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Image
        fields = (
            'title',
            'is_active',
            'image',
            'post',
            'created_date',
            'updated_date',
        )


class VideoSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Video
        fields = (
            'title',
            'is_active',
            'video',
            'post',
            'created_date',
            'updated_date',
        )
