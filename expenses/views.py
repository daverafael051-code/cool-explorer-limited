from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm

@login_required(login_url='/admin/login/')
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ExpenseForm()

    return render(request, 'expenses/add_expense.html', {'form': form})
