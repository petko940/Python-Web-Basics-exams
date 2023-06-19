from django.shortcuts import render

from October_30_2022.cars.models import Car
from October_30_2022.profiles.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.order_by('pk')

    context = {
        'cars': cars,
        'profile': profile
    }
    return render(request, 'common/catalogue.html',context)