from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for learning logs."""
    return render(request, "MaybornApp/index.html")
