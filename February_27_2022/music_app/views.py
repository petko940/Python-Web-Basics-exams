from django.shortcuts import render, redirect

from music_app.forms import ProfileForm, AlbumForm
from music_app.models import Profile, Album


# Create your views here.
def check_for_profile(request):
    profile = Profile.objects.all()
    if not profile:
        return home_no_profile(request)
    else:
        return home_with_profile(request)


def home_no_profile(request):
    profile = Profile.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return home_with_profile(request)
    else:
        form = ProfileForm()

        placeholders = {'username': 'Username',
                        'email': 'Email',
                        'age': 'Age'}

        for field in form.fields:
            form.fields[field].widget.attrs['placeholder'] = placeholders.get(field, '')

    context = {'form': form,
               'profile': profile}
    return render(request, 'home-no-profile.html', context)


def home_with_profile(request):
    album = Album.objects.all()
    for a in album:
        a.price = str(f"{a.price:.2f}")

    context = {'album': album}
    return render(request, 'home-with-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return home_with_profile(request)
    else:
        form = AlbumForm()

        placeholders = ["Album Name", "Artist", "", "Description", "Image URL", "Price"]
        for field, placeholder in zip(form.fields, placeholders):
            form.fields[field].widget.attrs['placeholder'] = placeholder

    context = {'form': form}
    return render(request, 'add-album.html', context)


def album_details(request, id):
    album = Album.objects.get(id=id)
    album.price = str(f"{album.price:.2f}")

    context = {'album': album}
    return render(request, 'album-details.html', context)


def album_edit(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return home_with_profile(request)
    else:
        form = AlbumForm(instance=album)

    context = {'album': album,
               'form': form}
    return render(request, 'edit-album.html', context)


def album_delete(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        album.delete()
        return home_with_profile(request)
    else:
        form = AlbumForm(instance=album)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

    context = {'album': album,
               'form': form}

    return render(request, 'delete-album.html', context)


def profile_details(request):
    # profile = Profile.objects.first()
    profile = Profile.objects.all()[0]
    number = len(Album.objects.all())

    context = {'profile': profile,
               'number': number}
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    album = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        album.delete()
        return redirect('check_for_profile')

    context = {'profile': profile,
               'album': album}
    return render(request, 'profile-delete.html', context)
