from django.urls import path

from August_2023_Retake_Eventer.events.views import DashboardPageView, CreateEventView, EventDetailsView, EditEventView, \
    DeleteEventView

urlpatterns = [
    path('dashboard', DashboardPageView.as_view(), name='dashboard'),
    path('create', CreateEventView.as_view(), name='create_event'),
    path('details/<int:pk>/', EventDetailsView.as_view(), name='details_event'),
    path('edit/<int:pk>/', EditEventView.as_view(), name='edit_event'),
    path('delete/<int:pk>/', DeleteEventView.as_view(), name='delete_event'),
]
