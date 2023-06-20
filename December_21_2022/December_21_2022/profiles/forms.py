from django import forms
from django.forms import ModelForm

from December_21_2022.profiles.models import Profile


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('username','first_name','last_name')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'label': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'label': 'Last Name'}),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
