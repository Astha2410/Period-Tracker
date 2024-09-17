from django.db import models
from datetime import timedelta


class Period(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    cycle_length = models.IntegerField(default=28)  # Default cycle length is 28 days

    @property
    def next_date(self):
        return self.start_date + timedelta(days=self.cycle_length)
