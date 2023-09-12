from django import forms
from django.core.validators import MinValueValidator


class ItemForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'item name',
        })
    )
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.0,
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 0.0}))
    amount = forms.IntegerField(min_value=0,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 0}))
    date_added = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    image = forms.ImageField()
