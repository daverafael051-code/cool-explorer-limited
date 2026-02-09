from django.urls import path
from .views import add_expense

urlpatterns = [
    path('add/', add_expense, name='add_expense'),
]
