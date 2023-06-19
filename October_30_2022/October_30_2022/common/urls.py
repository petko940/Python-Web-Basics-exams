from django.urls import path

from .views import index, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
]
