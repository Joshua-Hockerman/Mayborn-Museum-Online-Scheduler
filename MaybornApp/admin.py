from django.contrib import admin

# Register your models here.
from .models import Topic, Schedule

admin.site.register(Topic)
admin.site.register(Schedule)
