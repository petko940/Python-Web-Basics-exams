from django.urls import path

from .views import car_create, car_details, car_edit, car_delete

urlpatterns = [
    path('create/', car_create, name='car_create'),
    path('details/<int:pk>/', car_details, name='car_details'),
    path('edit/<int:pk>/', car_edit, name='car_edit'),
    path('delete/<int:pk>/', car_delete, name='car_delete'),
]
