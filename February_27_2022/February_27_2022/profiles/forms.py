from django import forms
from django.forms import ModelForm

from February_27_2022.profiles.models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
        }
