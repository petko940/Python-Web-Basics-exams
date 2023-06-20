from django.urls import path
from .views import home, catalogue

urlpatterns = [
    path('', home, name='home'),
    path('cataloge/', catalogue, name='catalogue'),
]
