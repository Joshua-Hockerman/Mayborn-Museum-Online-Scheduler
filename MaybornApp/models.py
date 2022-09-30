from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Schedule(models.Model):
    """A place for the employee to enter their holiday preference information"""

    Holiday_1 = models.SmallIntegerField()
    Holiday_2 = models.SmallIntegerField()
    Holiday_3 = models.SmallIntegerField()
    Holiday_4 = models.SmallIntegerField()
    Holiday_5 = models.SmallIntegerField()
    Holiday_6 = models.SmallIntegerField()
    Holiday_7 = models.SmallIntegerField()
    Holiday_8 = models.SmallIntegerField()
    Holiday_9 = models.SmallIntegerField()
    Holiday_10 = models.SmallIntegerField()

    Comments = models.CharField(max_length=500)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
