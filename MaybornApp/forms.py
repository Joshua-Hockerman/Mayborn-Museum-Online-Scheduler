from django import forms

from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = {
            "Holiday_1",
            "Holiday_2",
            "Holiday_3",
            "Holiday_4",
            "Holiday_5",
            "Holiday_6",
            "Holiday_7",
            "Holiday_8",
            "Holiday_9",
            "Holiday_10",
            "Comments",
        }
        labels = {
            "Holiday_1": "New Years Day",
            "Holiday_2": "MLK Day",
            "Holiday_3": "President's Day",
            "Holiday_4": "Memorial Day",
            "Holiday_5": "Juneteenth",
            "Holiday_6": "Independence Day",
            "Holiday_7": "Labor Day",
            "Holiday_8": "Veteran's Day",
            "Holiday_9": "Thanksgiving Day",
            "Holiday_10": "Christmas Day",
            "Comments": "Comments",
        }
