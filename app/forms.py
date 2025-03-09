from django.forms import Form
from django import forms

class OrderForm(Form):
    adres = forms.CharField(label='Адрес доставки')
    email = forms.EmailField(label='Email')
    telephone = forms.CharField(label='Telephone')
    nerobot = forms.BooleanField(label='не робот')