from django.urls import path

from August_2023_Retake_Eventer.accounts.views import CreateProfileView, details_profile, edit_profile, delete_profile

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', details_profile, name='details_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_profile, name='delete_profile'),
]
