from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)

class Period(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    cycle_length = models.IntegerField()
    
class Reminder(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    date = models.DateField()
    message = models.TextField()


    
