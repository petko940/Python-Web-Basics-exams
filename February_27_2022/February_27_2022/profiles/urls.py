from django.urls import path
from .views import profile_details,profile_delete

urlpatterns = [
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/delete', profile_delete, name='profile_delete'),
]
