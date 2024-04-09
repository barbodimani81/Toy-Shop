# from django.contrib.auth import get_user_model
# from rest_framework import serializers
#
# User = get_user_model()
#
#
# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#
