from django import forms
from django.forms import ModelForm

from October_30_2022.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
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
