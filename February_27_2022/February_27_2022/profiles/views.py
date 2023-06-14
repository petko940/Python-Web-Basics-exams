from django.shortcuts import render, redirect

from February_27_2022.albums.models import Album
from February_27_2022.profiles.models import Profile


# Create your views here.
def profile_details(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    context = {
        "profile": profile,
        'albums': albums,
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home')

    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile-delete.html', context)
