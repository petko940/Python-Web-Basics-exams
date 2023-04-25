from django.shortcuts import render, redirect

from games_app.forms import ProfileForm, GameForm, ProfileFormFirst
from games_app.models import Profile, Game


# Create your views here.
def base(request):
    profile = Profile.objects.all()[0]
    context = {'profile': profile}
    return render(request, 'base.html', context)


def home(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'home-page.html', context)


def profile_create(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileFormFirst(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileFormFirst()

    context = {'form': form,
               'profile': profile}
    return render(request, 'create-profile.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = Profile.objects.all()[0]

    context = {'games': games,
               'profile': profile}
    return render(request, 'dashboard.html', context)


def game_create(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm()

    context = {'profile': profile,
               'form': form}
    return render(request, 'create-game.html', context)


def game_details(request, id):
    profile = Profile.objects.all()[0]
    game = Game.objects.get(id=id)
    context = {'profile': profile,
               'game': game}
    return render(request, 'details-game.html', context)


def game_edit(request, id):
    profile = Profile.objects.all()[0]
    game = Game.objects.get(id=id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm(instance=game)

    context = {'profile': profile,
               'game': game,
               'form': form}
    return render(request, 'edit-game.html', context)


def game_delete(request, id):
    profile = Profile.objects.all()[0]
    game = Game.objects.get(id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')
    else:
        form = GameForm(instance=game)
        for x in form.fields:
            form.fields[x].widget.attrs['disabled'] = 'disabled'

    context = {'profile': profile,
               'game': game,
               'form': form}
    return render(request, 'delete-game.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    games = Game.objects.all()
    number_games = len(games)
    rating = sum(x.rating for x in games)
    average_rating = 0
    if number_games != 0:
        average_rating = rating / number_games

    context = {'profile': profile,
               'number_games': number_games,
               'average_rating': average_rating,
               'games': games}
    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileForm(instance=profile)

    context = {'profile': profile,
               'form': form}
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    games = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home')

    context = {'profile': profile,
               'games': games}
    return render(request, 'delete-profile.html', context)
