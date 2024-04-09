from django.urls import path
from .views import add_to_basket, view_basket

urlpatterns = [
    path('add_basket/', add_to_basket, name='add_to_basket'),
    path('basket/', view_basket, name='basket'),
]
