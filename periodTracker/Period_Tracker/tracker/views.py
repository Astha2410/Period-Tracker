from django.shortcuts import render
from .models import User,Period,Reminder

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request,'tracker/user_list.html',{'users':users})

def period_list(request):
    periods = Period.objects.all()
    return render(request,'tracker/period_list.html',{'periods':periods})

def reminder_list(request):
    reminders = Reminder.objects.all()
    return render(request,'tracker/reminder_list.html',{'reminders':reminders})
