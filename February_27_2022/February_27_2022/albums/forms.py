from django import forms
from django.forms import ModelForm

from February_27_2022.albums.models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "album_name": forms.TextInput(
                attrs={
                    "placeholder": "Album Name"
                }
            ),
            "artist": forms.TextInput(
                attrs={
                    "placeholder": "Artist"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Description"
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "Image URL"
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Price"
                }
            )

        }
        labels = {
            "album_name": "Album Name",
            "image_url": "Image URL",
        }


class AlbumDeleteForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
