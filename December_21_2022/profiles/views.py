from django.shortcuts import render, redirect

from plants.models import Plant
from profiles.forms import ProfileForm, EditProfileForm
from profiles.models import Profile


# Create your views here.
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.all()[0]
    plants = Plant.objects.all()

    context = {'profile': profile,
               'plants': len(plants)}
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details_profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {'profile': profile,
               'form': form}
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    plants = Plant.objects.all()
    if request.method == "POST":
        profile.delete()
        plants.delete()
        return redirect('index')

    context = {'profile':profile,
               'plants':plants}
    return render(request, 'delete-profile.html', context)
