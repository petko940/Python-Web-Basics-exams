from django import forms
from django.forms import ModelForm

from December_21_2022.plants.models import Plant


class CreatePlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        labels = {
            'plant_type': "Type",
            'image_url': "Image URL",
        }
