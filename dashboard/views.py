from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from categories.models import Category

# Create your views here.

@login_required
def dashboard_view(request):
    categories = Category.objects.all()
    return render(request, "dashboard/dashboard.html", {"categories": categories})
