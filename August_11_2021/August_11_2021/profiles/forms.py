from django import forms
from django.forms import ModelForm, TextInput, URLInput

from August_11_2021.profiles.models import Profile


class ProfileForm(ModelForm):
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder': 'Last Name'}))
    image_url = forms.URLField(widget=URLInput(attrs={'placeholder': 'URL'}))

    class Meta:
        model = Profile
        fields = '__all__'
