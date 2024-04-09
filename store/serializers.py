from rest_framework import serializers

from .models import Category, Product, Comment, Image, Video


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


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = (
            'title',
            'is_active',
            'description',
            'category',
            'created_date',
            'updated_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Comment
        fields = (
            'title',
            'is_active',
            'description',
            'created_date',
            'product',
            'updated_date',
        )


class ImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Image
        fields = (
            'title',
            'is_active',
            'image',
            'product',
            'created_date',
            'updated_date',
        )


class VideoSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Video
        fields = (
            'title',
            'is_active',
            'video',
            'product',
            'created_date',
            'updated_date',
        )
