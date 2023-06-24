from django.shortcuts import render, redirect

from June_24_2023_regular_exam.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from June_24_2023_regular_exam.fruits.models import Fruit
from June_24_2023_regular_exam.profiles.models import Profile


# Create your views here.
def fruit_create(request):
    form = FruitCreateForm()

    if request.method == "POST":
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': Profile.objects.first(),
    }
    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'profile': Profile.objects.first(),
        'fruit': fruit,
    }
    return render(request, 'fruits/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitEditForm(instance=fruit)

    if request.method == "POST":
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': Profile.objects.first(),
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitDeleteForm(instance=fruit)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    if request.method == "POST":
        fruit.delete()
        return redirect('dashboard')

    context = {
        'profile': Profile.objects.first(),
        "form": form,
    }
    return render(request, 'fruits/delete-fruit.html', context)
