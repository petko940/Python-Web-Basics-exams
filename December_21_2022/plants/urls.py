from django.urls import path

from plants import views

urlpatterns = [
    path('create', views.create_plant, name='create_plant'),
    path('details/<int:id>', views.details_plant, name='details_plant'),
    path('edit/<int:id>', views.edit_plant, name='edit_plant'),
    path('delete/<int:id>', views.delete_plant, name='delete_plant'),
]
