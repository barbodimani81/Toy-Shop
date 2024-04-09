from django.db import models

from blog.models import MyBaseModel


class User(MyBaseModel):
    username = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    password1 = models.CharField(max_length=255, null=False, blank=False)
    password2 = models.CharField(max_length=255, null=False, blank=False)
