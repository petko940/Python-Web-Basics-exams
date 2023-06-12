from django.urls import path
from .views import add_book, edit_book, details_book, delete_book

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>', edit_book, name='edit_book'),
    path('details/<int:pk>', details_book, name='details_book'),
    path('delete/<int:pk>', delete_book, name='delete_book'),
]
