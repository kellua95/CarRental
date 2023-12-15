from django import forms
from django.forms import ModelForm, TextInput
from .models import Cars, Custoumer

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'



class OrderForm(ModelForm):
    class Meta:
        model = Custoumer
        fields = '__all__'
        widgets = {
            'car': forms.HiddenInput(),
        }
