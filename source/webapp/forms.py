from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import ProductsChoice


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, widget=widgets.Textarea, label='Описание')
    image = forms.CharField(max_length=300, required=True, label='Фото')
    category = forms.ChoiceField(choices=ProductsChoice.choices, required=True, label='Категория')
    remaining = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Стоимость')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Поле name должно иметь не менее 3 символов')
        return name
