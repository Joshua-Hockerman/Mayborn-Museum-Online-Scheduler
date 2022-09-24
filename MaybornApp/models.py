from django.db import models

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


OPTION_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)


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
