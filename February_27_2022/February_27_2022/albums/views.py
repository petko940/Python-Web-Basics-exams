from django.shortcuts import render, redirect

from February_27_2022.albums.forms import AlbumForm
from February_27_2022.albums.models import Album
from February_27_2022.profiles.models import Profile


# Create your views here.
def album_add(request):
    form = AlbumForm()

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'albums/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'profile': Profile.objects.first(),
        'album': album
    }
    return render(request, 'albums/album-details.html', context)


def album_edit(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(pk=pk)

    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'profile': profile,
        'album': album,
        'form': form,
    }
    return render(request, 'albums/edit-album.html', context)


def album_delete(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)
    for field in form.fields:
        form.fields[field].disabled = True

    if request.method == 'POST':
        album.delete()
        return redirect('home')

    context = {
        'form': form,
        'profile': profile,
        'album': album
    }
    return render(request, 'albums/delete-album.html', context)
