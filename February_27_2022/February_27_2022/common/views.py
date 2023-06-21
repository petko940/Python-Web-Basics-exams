from django import forms
from django.shortcuts import render, redirect

from February_27_2022.albums.models import Album
from February_27_2022.profiles.forms import CreateProfileForm
from February_27_2022.profiles.models import Profile


# Create your views here.

def home(request):
    profile = Profile.objects.all()
    if not profile:
        form = CreateProfileForm()

        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

        context = {
            'form': form
        }
        return render(request, 'common/home-no-profile.html', context)

    albums = Album.objects.order_by('pk')

    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'common/home-with-profile.html', context)
