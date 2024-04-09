from .models import Product, Basket
from django.shortcuts import render, redirect
from .forms import BasketForm
from django.db.models import F


def add_to_basket(request, product_id=None):
    basket, _ = Basket.objects.get_or_create(pk=request.session.get('basket_id'))

    if product_id:
        # Adding product to basket via URL parameter
        product = Product.objects.get(pk=product_id)
        basket.products.add(product)
        return redirect('basket')
    elif request.method == 'POST':
        # Adding product to basket via form submission
        form = BasketForm(request.POST)
        if form.is_valid():
            products = form.cleaned_data['products']
            basket.products.add(*products)
            return redirect('basket')

    # If the request is neither a POST nor with a product_id, render the form
    form = BasketForm()
    return render(request, 'add_to_basket.html', {'form': form})


def view_basket(request):
    basket, _ = Basket.objects.get_or_create(pk=request.session.get('basket_id'))
    return render(request, 'basket.html', {'basket': basket})
