from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_if_there_is_profile, name='check_if_there_is_profile'),
    # path('', views.home_no_profile, name='home_no_profile'),
    # path('', views.home_with_profile, name='home_with_profile'),

    path('add', views.add_book, name='add'),
    path('detail/<int:id>', views.detail_book, name='detail_book'),
    path('edit/<int:id>', views.edit_book, name='edit_book'),
    path('delete/<int:id>', views.delete_book, name='delete_book'),

    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
]
