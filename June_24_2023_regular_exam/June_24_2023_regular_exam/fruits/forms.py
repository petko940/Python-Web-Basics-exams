from django import forms
from django.forms import ModelForm

from June_24_2023_regular_exam.fruits.models import Fruit


class FruitCreateForm(ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Fruit Name'}
            ),
            'image_url': forms.URLInput(
                attrs={'placeholder': 'Fruit Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description'}
            ),
            'nutrition': forms.Textarea(
                attrs={'placeholder': 'Nutrition Info'}
            ),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }


class FruitEditForm(ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description')
