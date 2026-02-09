from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import Member
from vehicles.models import Vehicle
from routes.models import Route
from trips.models import Trip
from expenses.models import Expense
from django.utils import timezone
from django.db.models import Sum
from drivers_app.models import Driver
from django.http import HttpResponseForbidden
from trips.models import Trip


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_clerk(user):
    return user.groups.filter(name='Clerk').exists()

def is_manager(user):
    return user.groups.filter(name='Manager').exists()


@login_required(login_url='/admin/login/')
def dashboard_home(request):
    today = timezone.now().date()

    context = {
        "total_members": Member.objects.count(),
        "total_vehicles": Vehicle.objects.count(),
        "total_routes": Route.objects.count(),
        "today_trips": Trip.objects.filter(trip_date=today).count(),
        "today_collection": Trip.objects.filter(trip_date=today).aggregate(
            Sum("revenue_collected")
        )["revenue_collected__sum"] or 0,
        "today_expenses": Expense.objects.filter(expense_date=today).aggregate(
            Sum("amount")
        )["amount__sum"] or 0,

        "total_drivers": Driver.objects.count(),
        "active_drivers": Driver.objects.filter(status='Active').count(),


        "is_admin": request.user.is_superuser,
        "is_clerk": request.user.groups.filter(name='Clerk').exists(),
        "is_manager": request.user.groups.filter(name='Manager').exists(),


    }


    return render(request, "dashboard/home.html", context)
from django.db.models import Sum
from django.utils import timezone

@login_required(login_url='/admin/login/')
def reports_view(request):
    selected_date = request.GET.get('date')
    selected_month = request.GET.get('month')

    trips = Trip.objects.all()
    expenses = Expense.objects.all()

    if selected_date:
        trips = trips.filter(trip_date=selected_date)
        expenses = expenses.filter(expense_date=selected_date)

    if selected_month:
        trips = trips.filter(trip_date__startswith=selected_month)
        expenses = expenses.filter(expense_date__startswith=selected_month)

    total_collections = trips.aggregate(
        Sum('revenue_collected')
    )['revenue_collected__sum'] or 0

    total_expenses = expenses.aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    net_balance = total_collections - total_expenses

    context = {
        'total_collections': total_collections,
        'total_expenses': total_expenses,
        'net_balance': net_balance,
    }

    return render(request, 'dashboard/reports.html', context)
from django.db.models import Count, Sum

@login_required(login_url='/admin/login/')
def driver_performance_report(request):
    if not request.user.groups.filter(name__in=['Admin', 'Manager']).exists():
        return HttpResponseForbidden("You are not allowed to view this report.")

    selected_date = request.GET.get('date')
    selected_month = request.GET.get('month')

    trips = Trip.objects.select_related('driver')

    if selected_date:
        trips = trips.filter(trip_date=selected_date)

    if selected_month:
        trips = trips.filter(trip_date__startswith=selected_month)

    report = trips.values(
        'driver__full_name'
    ).annotate(
        total_trips=Count('id'),
        total_revenue=Sum('revenue_collected')
    ).order_by('-total_revenue')

    context = {
        'report': report,
    }

    return render(request, 'dashboard/driver_report.html', context)
from auditlog.models import AuditLog

@login_required(login_url='/admin/login/')
def audit_logs_view(request):
    if not request.user.is_superuser and not request.user.groups.filter(name='Manager').exists():
        return HttpResponseForbidden("You are not allowed to view audit logs.")

    logs = AuditLog.objects.select_related('user').order_by('-timestamp')[:100]

    return render(request, 'dashboard/audit_logs.html', {'logs': logs})
from django.db.models import Count, Sum
from vehicles.models import Vehicle

@login_required(login_url='/admin/login/')
def vehicle_performance_report(request):
    # Only Admin & Manager
    if not request.user.is_superuser and not request.user.groups.filter(name='Manager').exists():
        return HttpResponseForbidden("You are not allowed to view this report.")

    selected_date = request.GET.get('date')
    selected_month = request.GET.get('month')

    trips = Trip.objects.select_related('vehicle')

    if selected_date:
        trips = trips.filter(trip_date=selected_date)

    if selected_month:
        trips = trips.filter(trip_date__startswith=selected_month)

    report = trips.values(
        'vehicle__id',
        'vehicle__plate_number'
    ).annotate(
        total_trips=Count('id'),
        total_revenue=Sum('revenue_collected')
    ).order_by('-total_revenue')

    return render(
        request,
        'dashboard/vehicle_report.html',
        {'report': report}
    )




