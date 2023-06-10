from django.urls import path

from .views import profile,delete_profile

urlpatterns = [
    path('profile', profile, name='profile'),
    path('profile-delete', delete_profile, name='delete_profile'),
]
