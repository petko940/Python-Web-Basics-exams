from django.urls import path
from .views import album_add, album_details, album_edit, album_delete

urlpatterns = [
    path('album/add/', album_add, name='album_add'),
    path('album/details/<int:pk>/', album_details, name='album_details'),
    path('album/edit/<int:pk>/', album_edit, name='album_edit'),
    path('album/delete/<int:pk>/', album_delete, name='album_delete'),

]
