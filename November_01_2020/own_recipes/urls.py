from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create.html', views.create, name='create'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('details/<int:id>/', views.details, name='details'),
]
