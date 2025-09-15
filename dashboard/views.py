from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_dashboard(request):
    return HttpResponse("Hello, Dashboard!")