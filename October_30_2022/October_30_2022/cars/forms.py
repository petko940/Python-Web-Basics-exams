from django.forms import ModelForm

from October_30_2022.cars.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
