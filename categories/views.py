from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_view(request):
    return HttpResponse("This is a test view for categories app") # Temporary response for testing
