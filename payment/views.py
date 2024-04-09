from django.shortcuts import render

from basket.models import Basket

from django.shortcuts import render
from django.http import HttpResponse


def payment_view(request, basket_id):
    try:
        basket = Basket.objects.get(id=basket_id)
    except Basket.DoesNotExist:
        return HttpResponse("Basket not found", status=404)

    return render(request, 'payment.html', {'basket': basket})


def payment_successful(request):
    return HttpResponse("Payment successful")


def payment_unsuccessful(request):
    return HttpResponse("Payment unsuccessful")
