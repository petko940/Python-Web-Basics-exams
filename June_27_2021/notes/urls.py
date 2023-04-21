from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_no_profile, name='home_no_profile'),
    path('', views.home_with_profile, name='home_with_profile'),
    path('add', views.note_create, name='add'),
    path('delete/<int:id>', views.note_delete, name='note_delete'),
    path('edit/<int:id>', views.note_edit, name='note_edit'),
    path('details/<int:id>', views.note_details, name='note_details'),

    path('profile', views.profile, name='profile'),
    path('prolile/delete', views.delete_profile, name='delete_profile'),
]
