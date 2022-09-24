from django.shortcuts import render, redirect

from .models import Schedule
from .forms import ScheduleForm

# Create your views here.


def index(request):
    """The home page for learning logs."""
    return render(request, "MaybornApp/index.html")


def schedule(request):
    """Allow the employee to enter the schedule"""
    if request.method != "POST":
        # No data submitted, create a blank form.
        form = ScheduleForm()
    else:
        # POST data submitted, process data
        form = ScheduleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("MaybornApp:index")

    context = {"form": form}
    return render(request, "MaybornApp/schedule.html", context)
