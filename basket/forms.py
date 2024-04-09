from django import forms
from .models import Product


class BasketForm(forms.Form):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for product in self.fields['products'].queryset:
            self.fields['products'].label_from_instance = lambda obj: f'{obj.title} - ${obj.price}'
