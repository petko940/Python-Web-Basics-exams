from django.shortcuts import render, redirect

from plants.forms import PlantForm
from plants.models import Plant
from profiles.models import Profile


# Create your views here.
def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm()
    context = {'form': form}
    return render(request, 'create-plant.html', context)


def details_plant(request, id):
    plant = Plant.objects.get(id=id)
    profile = Profile.objects.all()
    context = {'plant': plant,
               'profile': profile}
    return render(request, 'plant-details.html', context)


def edit_plant(request, id):
    plant = Plant.objects.get(id=id)
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm(instance=plant)

    context = {'plant': plant,
               'profile': profile,
               'form': form}
    return render(request, 'edit-plant.html', context)


def delete_plant(request, id):
    plant = Plant.objects.get(id=id)
    profile = Profile.objects.all()
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = PlantForm(instance=plant)
    for x in form.fields.values():
        x.widget.attrs['disabled'] = 'disabled'

    context = {'plant': plant,
               'profile': profile,
               'form': form}
    return render(request, 'delete-plant.html', context)
