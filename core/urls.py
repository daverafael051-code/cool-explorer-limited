from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # 👈 THIS IS CRITICAL
    path('trips/', include('trips.urls')),
    path('expenses/', include('expenses.urls')),
]
