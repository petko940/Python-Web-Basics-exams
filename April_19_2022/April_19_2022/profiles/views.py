from django.shortcuts import render, redirect

from April_19_2022.games.models import Game
from April_19_2022.profiles.forms import ProfileCreateForm, ProfileEditForm
from April_19_2022.profiles.models import Profile


# Create your views here.
def profile_create(request):
    form = ProfileCreateForm()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    games = Game.objects.all()

    average_rating = 0
    for game in games:
        average_rating += game.rating

    if games:
        average_rating /= games.count()

    context = {
        'profile': profile,
        'games': games,
        'average_rating': average_rating
    }
    return render(request, 'profiles/details-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    games = Game.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home')

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/delete-profile.html', context)

