from django.forms import ModelForm

from April_19_2022.games.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
