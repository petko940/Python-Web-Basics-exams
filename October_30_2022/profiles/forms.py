from django import forms
from django.forms import ModelForm

from profiles.models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
