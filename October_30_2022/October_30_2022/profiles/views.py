from django.shortcuts import render, redirect

from October_30_2022.cars.models import Car
from October_30_2022.profiles.forms import ProfileForm, ProfileEditForm
from October_30_2022.profiles.models import Profile


# Create your views here.

def profile_create(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    cars = Car.objects.all()

    sum_car = sum([x.price for x in cars])
    context = {
        'profile': profile,
        'sum_car': sum_car,
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    car = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        car.delete()
        return redirect('index')

    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile-delete.html', context)
