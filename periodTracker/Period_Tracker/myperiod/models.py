from django.db import models
from django.contrib.auth.models import User

class PeriodData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    period_length = models.IntegerField()
    cycle_length = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s period data"
