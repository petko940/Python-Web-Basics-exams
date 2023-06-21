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
        'album': album,
        "profile": Profile.objects.first()
    }
    return render(request, 'albums/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'albums/edit-album.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == 'POST':
        album.delete()
        return redirect('home')

    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'albums/delete-album.html', context)
