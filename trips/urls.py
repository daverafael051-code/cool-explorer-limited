from django.urls import path
from .views import add_trip

urlpatterns = [
    path('add/', add_trip, name='add_trip'),
]
