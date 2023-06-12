from django.urls import path
from .views import profile_page, edit_profile, delete_profile

urlpatterns = [
    path('profile/', profile_page, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
