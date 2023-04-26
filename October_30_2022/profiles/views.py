from django.shortcuts import render, redirect

from cars.models import Car
from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile


# Create your views here.
def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {'form': form}
    return render(request, 'profile-create.html', context)


def profile_details(request):
    profile = Profile.objects.all()[0]
    cars = Car.objects.all()
    total_price = sum(x.price for x in cars)
    context = {'profile': profile,
               'total_price': total_price}
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = EditProfileForm(instance=profile)

    context = {'profile': profile,
               'form': form}
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.all()[0]
    cars = Car.objects.all()
    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('index')

    context = {'profile': profile}
    return render(request, 'profile-delete.html', context)
