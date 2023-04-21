from django.shortcuts import render, redirect

from notes.forms import ProfileForm, NoteForm
from notes.models import Profile, Note


# Create your views here.


def home_no_profile(request):
    profile = Profile.objects.all()
    notes = Note.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_with_profile')
    else:
        form = ProfileForm()

    context = {'form': form,
               'profile': profile,
               "notes": notes}

    return render(request, 'home-with-profile.html', context)


def home_with_profile(request):
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'home-with-profile.html', {'profile': profile})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_with_profile')
    else:
        form = NoteForm()

    context = {'form': form,
               'profile': profile, }

    return render(request, 'note-create.html', context)


def note_delete(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('home_no_profile')

    context = {'note': note}
    return render(request, 'note-delete.html', context)


def note_details(request, id):
    note = Note.objects.get(id=id)
    context = {'note': note}
    return render(request, 'note-details.html', context)


def note_edit(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', note.content)
        image_url = request.POST.get('image_url')

        note.title = title
        note.content = content
        note.image_url = image_url

        note.save()
        return redirect('home_no_profile')

    context = {'note': note}
    return render(request, 'note-edit.html', context)


def profile(request):
    profile = Profile.objects.all()
    note = Note.objects.all()

    context = {"profile": profile[0],
               "note": len(note)}

    return render(request, 'profile.html', context)


def delete_profile(request):
    Profile.objects.all().delete()
    Note.objects.all().delete()
    return redirect('home_no_profile')
