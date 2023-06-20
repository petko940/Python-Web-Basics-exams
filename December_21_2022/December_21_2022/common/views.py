from django.shortcuts import render

from December_21_2022.plants.models import Plant
from December_21_2022.profiles.models import Profile


# Create your views here.
def home(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/home-page.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    plants = Plant.objects.order_by('pk')

    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'common/catalogue.html', context)
