from django.urls import path

from profiles import views

urlpatterns = [
    path('profile/create', views.profile_create, name='profile_create'),
    path('profile/details', views.profile_details, name='profile_detail'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
]
