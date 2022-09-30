from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Schedule
from .forms import ScheduleForm

# Create your views here.


def index(request):
    """The home page for learning logs."""
    return render(request, "MaybornApp/index.html")


@login_required
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


@login_required
def edit_schedule(request, schedule_id):
    """Allow the user to edit their entry in case of a change of mind"""
    schedule = Schedule.objects.get(id=schedule_id)

    if request.method != "POST":
        # Call up the schedule from the database
        form = ScheduleForm(instance=schedule)

    else:
        # POST data submitted; process data
        form = ScheduleForm(instance=schedule, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("MaybornApp:index", schedule=schedule.id)

    context = {"schedule": schedule, "form": form}
    return render(request, "MaybornApp/edit_schedule.html", context)


@login_required
def admin_page(request):
    """
    Compiles the information submitted by the employees in the database
    and displays it in a data grid view.  Allows for the admin to compile
    the employee schedules through the algorithm and send out the compiled
    schedule to employees
    """
    schedules = Schedule.objects.all()

    context = {"schedules": schedules}
    return render(request, "MaybornApp/admin_page.html", context)
