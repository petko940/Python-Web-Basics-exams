from django.shortcuts import render

from April_19_2022.games.models import Game
from April_19_2022.profiles.models import Profile


# Create your views here.
def home(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'profile': Profile.objects.first(),
        'games': games
    }
    return render(request, 'common/dashboard.html',context)
