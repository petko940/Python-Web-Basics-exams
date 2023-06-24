from django.shortcuts import render, redirect

from June_24_2023_regular_exam.fruits.models import Fruit
from June_24_2023_regular_exam.profiles.forms import CreateProfileForm, EditProfileForm
from June_24_2023_regular_exam.profiles.models import Profile


# Create your views here.
def profile_create(request):
    profile = Profile.objects.all()
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, "profiles/create-profile.html", context)


def profile_details(request):
    fruits_count = Fruit.objects.all().count()

    context = {
        'profile': Profile.objects.all()[0],
        'fruits_count': fruits_count
    }
    return render(request, "profiles/details-profile.html", context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, "profiles/edit-profile.html", context)


def profile_delete(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    context = {
        'profile': profile
    }
    return render(request, "profiles/delete-profile.html", context)
