from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PeriodData

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ["username", "name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["name"]
        if commit:
            user.save()
        return user

class PeriodDataForm(forms.ModelForm):
    class Meta:
        model = PeriodData
        fields = ['start_date', 'period_length', 'cycle_length']
