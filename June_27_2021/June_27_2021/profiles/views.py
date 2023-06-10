from django.shortcuts import render, redirect

from June_27_2021.notes.models import Note
from June_27_2021.profiles.models import Profile


# Create your views here.
def profile(request):
    profil = Profile.objects.first()
    notes = Note.objects.all()

    context = {
        'profile': profil,
        'notes': notes,
    }
    return render(request, 'profiles/profile.html', context)


def delete_profile(request):
    Profile.objects.first().delete()
    Note.objects.all().delete()
    return redirect('home')

