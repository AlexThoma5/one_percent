from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from categories.models import Category

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('landing')


@login_required
def dashboard_view(request):
    categories = Category.objects.all()
    return render(request, "dashboard/dashboard.html", {"categories": categories})


def landing_view(request):
    return render(request, "dashboard/landing.html")
