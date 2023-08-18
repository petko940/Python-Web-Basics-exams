from django.urls import path

from August_2023_Retake_Eventer.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
