# views.py
from django.shortcuts import render
from .forms import PeriodForm
from datetime import timedelta

def period_view(request):
    next_date = None
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            period = form.save(commit=False)
            next_date = period.next_date
    else:
        form = PeriodForm()

    return render(request, 'period/index.html', {'form': form, 'next_date': next_date})
