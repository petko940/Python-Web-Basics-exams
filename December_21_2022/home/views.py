from django.shortcuts import render

from plants.models import Plant
from profiles.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = Profile.objects.all()
    plants = Plant.objects.all()
    context = {'profile': profile,
               'plants': plants}

    return render(request, 'catalogue.html', context)
