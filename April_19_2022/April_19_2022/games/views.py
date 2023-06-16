from django.shortcuts import render, redirect

from April_19_2022.games.forms import GameForm
from April_19_2022.games.models import Game
from April_19_2022.profiles.models import Profile


# Create your views here.
def game_create(request):
    profile = Profile.objects.first()
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'games/create-game.html', context)


def game_details(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'games/details-game.html', context)


def game_edit(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form
    }
    return render(request, 'games/edit-game.html', context)


def game_delete(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    form = GameForm(instance=game)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == "POST":
        game.delete()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form
    }
    return render(request, 'games/delete-game.html', context)
