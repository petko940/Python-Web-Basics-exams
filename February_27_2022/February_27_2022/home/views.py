from django.shortcuts import render

from February_27_2022.albums.models import Album
from February_27_2022.profiles.forms import ProfileForm
from February_27_2022.profiles.models import Profile


# Create your views here.

def home(request):
    profile = Profile.objects.all()
    if not profile:
        return without_profile(request)

    return with_profile(request)


def without_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return with_profile(request)
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def with_profile(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)
