from django.contrib import admin
from .models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "route", "trip_date", "revenue_collected")
