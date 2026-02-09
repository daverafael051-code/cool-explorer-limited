from django.urls import path
from .views import (
    dashboard_home,
    reports_view,
    driver_performance_report,
    audit_logs_view,
)
from .views import (
    dashboard_home,
    reports_view,
    driver_performance_report,
    audit_logs_view,
    vehicle_performance_report,
)


urlpatterns = [
    path('', dashboard_home, name='dashboard'),
    path('reports/', reports_view, name='reports'),
    path('drivers-report/', driver_performance_report, name='drivers_report'),
    path('vehicle-report/', vehicle_performance_report, name='vehicle_report'),
    path('audit-logs/', audit_logs_view, name='audit_logs'),
    
]
