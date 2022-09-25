"""Defines URL patterns for the users"""

from django.urls import path, include

app_name = "users"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
