from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PeriodDataForm
from .models import PeriodData
from datetime import timedelta

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('update_period')  # Redirect to update_period after registration
    else:
        form = RegistrationForm()
    return render(request, 'myperiod/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'myperiod/login.html', {'form': form})

@login_required
def profile(request):
    try:
        period_data = PeriodData.objects.get(user=request.user)
        # Calculate period dates
        start_date = period_data.start_date
        period_length = period_data.period_length
        cycle_length = period_data.cycle_length

        # Generate period dates from the next month onwards
        import datetime
        today = datetime.date.today()
        next_month = today.replace(day=28) + datetime.timedelta(days=4)
        next_month_start = next_month - datetime.timedelta(days=next_month.day - 1)
        
        period_dates = []
        while start_date < next_month_start:
            start_date += datetime.timedelta(days=cycle_length)

        for i in range(12):  # Display periods for the next 12 cycles
            period_dates.append({
                'start': start_date,
                'end': start_date + datetime.timedelta(days=period_length)
            })
            start_date += datetime.timedelta(days=cycle_length)

        next_period_date = period_data.start_date + timedelta(days=period_data.cycle_length)
    except PeriodData.DoesNotExist:
        period_data = None
        period_dates = []
        next_period_date = None

    return render(request, 'myperiod/profile.html', {
        'period_data': period_data,
        'period_dates': period_dates,
        'user_name': request.user.first_name,
        'next_period_date': next_period_date
    })

@login_required
def update_period(request):
    try:
        period_data = PeriodData.objects.get(user=request.user)
    except PeriodData.DoesNotExist:
        period_data = None

    if request.method == 'POST':
        form = PeriodDataForm(request.POST, instance=period_data)
        if form.is_valid():
            period_data = form.save(commit=False)
            period_data.user = request.user
            period_data.save()
            next_period_date = period_data.start_date + timedelta(days=period_data.cycle_length)
            return redirect('profile')
    else:
        form = PeriodDataForm(instance=period_data)

    return render(request, 'myperiod/update_period.html', {'form': form})
