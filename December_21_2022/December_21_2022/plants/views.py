from django.shortcuts import render, redirect

from December_21_2022.plants.forms import CreatePlantForm
from December_21_2022.plants.models import Plant
from December_21_2022.profiles.models import Profile


# Create your views here.

def create_plant(request):
    profile = Profile.objects.all()[0]
    form = CreatePlantForm()
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'plants/create-plant.html', context)


def details_plant(request, pk):
    profile = Profile.objects.all()[0]
    plant = Plant.objects.get(pk=pk)

    context = {
        'plant': plant,
        'profile': profile
    }
    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, pk):
    profile = Profile.objects.all()[0]
    plant = Plant.objects.get(pk=pk)
    form = CreatePlantForm(instance=plant)

    if request.method == 'POST':
        form = CreatePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    profile = Profile.objects.all()[0]
    plant = Plant.objects.get(pk=pk)
    form = CreatePlantForm(instance=plant)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'plants/delete-plant.html', context)
