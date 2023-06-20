from django.urls import path
from .views import create_plant, details_plant, edit_plant, delete_plant

urlpatterns = [
    path('create/', create_plant, name='create_plant'),
    path('details/<int:pk>/', details_plant, name='details_plant'),
    path('edit/<int:pk>/', edit_plant, name='edit_plant'),
    path('delete/<int:pk>/', delete_plant, name='delete_plant'),
]
