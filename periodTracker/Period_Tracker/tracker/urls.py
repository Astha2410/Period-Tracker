from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.user_list,name='user_list'),
    path('periods/',views.period_list,name = 'period_list'),
    path('reminders/',views.reminder_list,name= 'reminder_list')
]