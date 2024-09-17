# urls.py
from django.urls import path
from .views import period_view

urlpatterns = [
    path('', period_view, name='period'),
]
