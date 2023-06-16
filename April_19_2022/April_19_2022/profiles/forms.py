from django import forms
from django.forms import ModelForm

from April_19_2022.profiles.models import Profile


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
