from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard_view(request):
    return HttpResponse("Welcome to One Percent - this is a placeholder.")  # Placeholder view for testing
