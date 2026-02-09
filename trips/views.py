from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TripForm
from django.http import HttpResponseForbidden


@login_required(login_url='/admin/login/')
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TripForm()

    return render(request, 'trips/add_trip.html', {'form': form})
