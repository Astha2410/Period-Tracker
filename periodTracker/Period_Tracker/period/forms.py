# forms.py
from django import forms
from .models import Period

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ['start_date', 'cycle_length']
