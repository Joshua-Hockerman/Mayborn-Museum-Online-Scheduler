"""Defines the URL patterns for the Mayborn App"""

from django.urls import path

from . import views

app_name = "MaybornApp"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("schedule/", views.schedule, name="schedule"),
]
