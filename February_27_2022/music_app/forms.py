from django import forms
from django.forms import ModelForm

from music_app.models import Profile, Album


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class AlbumForm(ModelForm):
    album_name = forms.CharField(label="Album Name")

    class Meta:
        model = Album
        fields = '__all__'
