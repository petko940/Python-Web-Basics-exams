from django import forms
from django.forms import ModelForm

from cars.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
