from django.shortcuts import render, redirect

from December_21_2022.plants.models import Plant
from December_21_2022.profiles.forms import CreateProfileForm, EditProfileForm
from December_21_2022.profiles.models import Profile


# Create your views here.
# profile_details, profile_edit, profile_delete, profile_create

def profile_create(request):
    form = CreateProfileForm()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    plants = Plant.objects.all()[:3]

    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    form = EditProfileForm(instance=Profile.objects.all()[0])

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=Profile.objects.all()[0])
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'form': form,
        'profile': Profile.objects.all()[0]
    }
    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'profiles/delete-profile.html', context)
