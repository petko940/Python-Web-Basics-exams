from django.shortcuts import render, redirect

from June_27_2021.notes.forms import NoteForm
from June_27_2021.notes.models import Note
from June_27_2021.profiles.forms import ProfileForm
from June_27_2021.profiles.models import Profile


# Create your views here.
def home(request):
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
            return redirect('home')
    form = ProfileForm()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def home_with_profile(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    profile = Profile.objects.all()[0]
    notes = Note.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NoteForm()

    context = {
        'profile': profile,
        'notes': notes,
        'form': form
    }
    return render(request, 'notes/note-create.html', context)


def edit_note(request, pk):
    profile = Profile.objects.all()[0]
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note = NoteForm(request.POST, instance=note)
        if note.is_valid():
            note.save()
            return redirect('home')
    form = NoteForm(instance=note)

    context = {
        'profile': profile,
        'notes': note,
        'form': form
    }
    return render(request, 'notes/note-edit.html', context)


def delete_note(request, pk):
    profile = Profile.objects.all()[0]
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('home')

    form = NoteForm(instance=note)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'notes/note-delete.html', context)


def details_note(request, pk):
    profile = Profile.objects.first()
    note = Note.objects.get(pk=pk)

    context = {
        'profile': profile,
        'note': note
    }
    return render(request, 'notes/note-details.html', context)
