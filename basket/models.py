from django.db import models

from blog.models import MyBaseModel
from store.models import Product


"""
1- there is always an empty basket
2- show all the products
3- add products to basket
4- click finalize and see all products and summed price
5- click pay and see: 'payment done'
"""


class Basket(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, default='sample')
    products = models.ManyToManyField(Product, related_name='baskets', blank=True)

    def total_price(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f'Basket {self.id}'

