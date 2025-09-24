from django.shortcuts import render
from django.http import HttpResponse
from categories.models import Category

# Create your views here.


def dashboard_view(request):
    categories = Category.objects.all()
    return render(request, "dashboard/dashboard.html", {"categories": categories})
