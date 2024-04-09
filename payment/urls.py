from django.urls import path
from . import views

urlpatterns = [
    path('basket/<int:basket_id>/', views.payment_view, name='payment_view'),
    path('payment/successful/', views.payment_successful, name='payment_successful'),
    path('payment/unsuccessful/', views.payment_unsuccessful, name='payment_unsuccessful'),
]
