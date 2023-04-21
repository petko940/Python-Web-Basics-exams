from django.shortcuts import render, redirect

from own_recipes.forms import RecipeForm
from own_recipes.models import Recipe


# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('index')

    else:
        form = RecipeForm()
    return render(request, 'create.html', {'form': form})


def edit(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit.html', {'form': form, 'recipe': recipe})


def delete(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    context = {
        'recipe': recipe,
        'id': id,
    }
    return render(request, 'delete.html', context)


def details(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.ingredients = recipe.ingredients.split(', ')
    return render(request, 'details.html', {'recipe': recipe, 'id': id})
