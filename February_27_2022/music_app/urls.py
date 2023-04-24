from django.urls import path

from music_app import views

urlpatterns = [
    path('', views.check_for_profile, name='check_for_profile'),

    path('album/add', views.album_add, name='album_add'),
    path('album/details/<int:id>', views.album_details, name='album_details'),
    path('album/edit/<int:id>', views.album_edit, name='album_edit'),
    path('album/delete/<int:id>', views.album_delete, name='album_delete'),

    path('profile/details', views.profile_details, name='profile_details'),
    path('profile/delete', views.profile_delete, name='profile_delete'),

]
