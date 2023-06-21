from django.shortcuts import render, redirect

from February_27_2022.albums.models import Album
from February_27_2022.profiles.models import Profile


# Create your views here.
def profile_details(request):
    profile = Profile.objects.all()[0]
    albums_count = Album.objects.all().count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    album = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        album.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'album': album,
    }
    return render(request, 'profiles/profile-delete.html', context)
