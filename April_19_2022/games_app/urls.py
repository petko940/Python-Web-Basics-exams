from django.urls import path

from games_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/create', views.profile_create, name='profile_create'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('game/create/', views.game_create, name='game_create'),
    path('game/details/<int:id>/', views.game_details, name='game_details'),
    path('game/edit/<int:id>/', views.game_edit, name='game_edit'),
    path('game/delete/<int:id>/', views.game_delete, name='game_delete'),

    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),

]
