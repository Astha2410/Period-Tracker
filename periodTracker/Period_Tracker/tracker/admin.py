from django.contrib import admin
from .models import User,Period,Reminder

# Register your models here.
admin.site.register(User)
admin.site.register(Period)
admin.site.register(Reminder)

