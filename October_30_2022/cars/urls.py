from django.urls import path

from cars import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue', views.catalogue, name='catalogue'),

    path('car/create', views.car_create, name='car_create'),
    path('car/<int:id>/details/ ', views.car_details, name='car_details'),
    path('car/<int:id>/edit/ ', views.car_edit, name='car_edit'),
    path('car/<int:id>/delete/ ', views.car_delete, name='car_delete'),
]
