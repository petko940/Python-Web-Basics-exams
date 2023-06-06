from django.shortcuts import render, redirect

from November012020.recipes.forms import RecipeForm
from November012020.recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = RecipeForm()
    context = {'form': form}
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    form = RecipeForm(instance=recipe)
    for field_name, field in form.fields.items():
        field.widget.attrs['disabled'] = 'disabled'
    context = {'form': form}
    return render(request, 'delete.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.ingredients = recipe.ingredients.split(', ')
    context = {"recipe": recipe}
    return render(request, 'details.html', context)
