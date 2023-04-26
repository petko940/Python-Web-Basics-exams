from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue', views.catalogue, name='catalogue'),
]
