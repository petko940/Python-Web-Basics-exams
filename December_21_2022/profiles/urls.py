from django.urls import path

from profiles import views

urlpatterns = [
    path('profile/create', views.create_profile, name='create_profile'),
    path('profile/details', views.details_profile, name='details_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/delete', views.delete_profile, name='delete_profile'),
]
