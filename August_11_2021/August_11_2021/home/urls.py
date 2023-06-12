from django.urls import path
from .views import check_if_there_is_profile

urlpatterns = [
    path('', check_if_there_is_profile, name='home')
]
