from django.urls import path

from November012020.recipes.views import index, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = [
    path('', index, name='index'),
    path('create', create_recipe, name='create_recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete_recipe'),
    path('details/<int:pk>', recipe_details, name='recipe_details'),
]
