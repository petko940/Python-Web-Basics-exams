from django.shortcuts import render, redirect

from cars.forms import CarForm
from cars.models import Car
from profiles.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.all()

    context = {'profile': profile}
    return render(request, 'index.html', context)


def catalogue(request):
    profile = Profile.objects.all()
    cars = Car.objects.all()
    total_cars = len(cars)
    context = {'profile': profile,
               'cars': cars,
               'total_cars': total_cars}
    return render(request, 'catalogue.html', context)


def car_create(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm()

    context = {'form': form,
               'profile': profile}
    return render(request, 'car-create.html', context)


def car_details(request, id):
    profile = Profile.objects.all()
    car = Car.objects.get(id=id)
    context = {'car': car,
               'profile': profile}
    return render(request, 'car-details.html', context)


def car_edit(request, id):
    profile = Profile.objects.all()
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm(instance=car)

    context = {'car': car,
               'profile': profile,
               'form': form}
    return render(request, 'car-edit.html', context)


def car_delete(request, id):
    profile = Profile.objects.all()
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    else:
        form = CarForm(instance=car)
        for x in form.fields:
            form.fields[x].widget.attrs['disabled'] = 'disabled'

    context = {'profile': profile,
               'car': car,
               'form': form}
    return render(request, 'car-delete.html', context)
