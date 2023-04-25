from django import forms
from django.forms import ModelForm

from games_app.models import Profile, Game


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {'password': forms.PasswordInput()}


class ProfileFormFirst(ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {'password': forms.PasswordInput()}


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
