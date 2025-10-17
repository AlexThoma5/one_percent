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

    # Chatgpt helped with chart.js setup
    labels = []
    data = []

    for category in categories:
        labels.append(category.name)
        data.append(category.logs.filter(user=request.user).count())

    return render(
        request,
        "dashboard/dashboard.html",
        {"categories": categories,
         "labels": labels,
         "data": data})


def landing_view(request):
    return render(request, "dashboard/landing.html")
