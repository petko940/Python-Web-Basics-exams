from django.forms import ModelForm

from plants.models import Plant


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
