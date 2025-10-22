from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from categories.models import Category

# Create your views here.


def home_view(request):
    """
    'home' redirects user to 'dashboard' if authenticated or 'landing'
    if they are not authenticated.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('landing')


@login_required
def dashboard_view(request):
    """
    Display the user's dashboard with all :model:`categories.Category` objects.

    **Context**

    ``categories``
        All instances of :model:`categories.Category`.
    ``log_count``
        A zipped iterable of each category name and the number of logs
        created by the current user.
    ``labels``
        A list of category names used for Chart.js data labels.
    ``data``
        A list of log counts corresponding to each category.

    **Template:**

    :template:`dashboard/dashboard.html`
    """
    categories = Category.objects.all()

    # Chatgpt helped with chart.js setup
    labels = []
    data = []

    for category in categories:
        labels.append(category.name)
        data.append(category.logs.filter(user=request.user).count())

    log_count = zip(labels, data)

    return render(
        request,
        "dashboard/dashboard.html",
        {"categories": categories,
         "log_count": log_count,
         "labels": labels,
         "data": data})


def landing_view(request):
    """
    Renders landing.html template
    """
    return render(request, "dashboard/landing.html")
