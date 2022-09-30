"""Defines the URL patterns for the Mayborn App"""

from django.urls import path

from . import views

app_name = "MaybornApp"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("schedule/", views.schedule, name="schedule"),
    path("edit_schedule/<int:schedule_id>/", views.edit_schedule, name="edit_schedule"),
    path("admin_page/", views.admin_page, name="admin_page"),
]
