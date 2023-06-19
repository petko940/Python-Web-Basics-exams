from django.shortcuts import render, redirect

from October_30_2022.cars.forms import CarForm
from October_30_2022.cars.models import Car
from October_30_2022.profiles.models import Profile


# Create your views here.
def car_create(request):
    profile = Profile.objects.first()
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'cars/car-create.html', context)


def car_details(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
        'profile': profile
    }
    return render(request, 'cars/car-details.html', context)


def car_edit(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)

    form = CarForm(instance=car)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'cars/car-edit.html', context)


def car_delete(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = CarForm(instance=car)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'cars/car-delete.html', context)
