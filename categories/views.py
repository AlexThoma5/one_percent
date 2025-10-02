from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Log

# Create your views here.


def test_view(request):
    return HttpResponse("This is a test view for categories app")  # Temporary response for testing


def category_detail(request, slug):
    """
    Display an individual :model:`categories.Category`.

    **Context**

    ``category``
        An instance of :model:`categories.Category`.
    ``logs``
        All logs in relation to the category`.
    **Template:**

    :template:`categories/category_detail.html`
    """

    queryset = Category.objects.all()
    category = get_object_or_404(queryset, slug=slug)
    logs = category.logs.all().order_by('-created_on')

    return render(
        request,
        "categories/category_detail.html",
        {"category": category,
         "logs": logs,
         },
    )
