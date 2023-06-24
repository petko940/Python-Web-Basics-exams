from django.shortcuts import render

from June_24_2023_regular_exam.fruits.models import Fruit
from June_24_2023_regular_exam.profiles.models import Profile


# Create your views here.
def index(request):
    context = {
        "profile": Profile.objects.all(),
    }
    return render(request, "common/index.html", context)


def dashboard(request):
    fruits = Fruit.objects.order_by('pk')

    context = {
        "profile": Profile.objects.first(),
        "fruits": fruits,
    }
    return render(request, "common/dashboard.html", context)
