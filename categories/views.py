from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Category, Log
from .forms import LogForm

# Create your views here.


def test_view(request):
    return HttpResponse("This is a test view for categories app")  # Temporary response for testing


@login_required
def category_detail(request, slug):
    """
    Display an individual :model:`categories.Category`.

    **Context**

    ``category``
        An instance of :model:`categories.Category`.
    ``logs``
        All logs in relation to the category tied to individual user`.
    ``log_form``
    An instance of :form:`categories.LogForm`
    **Template:**

    :template:`categories/category_detail.html`
    """

    queryset = Category.objects.all()
    category = get_object_or_404(queryset, slug=slug)
    logs = category.logs.filter(user=request.user).order_by('-created_on')

    if request.method == "POST":
        log_form = LogForm(data=request.POST)
        if log_form.is_valid():
            log = log_form.save(commit=False)
            log.user = request.user
            log.category = category
            log.save()
            messages.add_message(request, messages.SUCCESS, 'Great job! Your new log has been added.')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong — but your effort still matters.')

    log_form = LogForm()
    edit_log_form = LogForm(prefix="edit")

    return render(
        request,
        "categories/category_detail.html",
        {"category": category,
         "logs": logs,
         "log_form": log_form,
         "edit_log_form": edit_log_form,
         },
    )


@login_required
def log_edit(request, slug, log_id):
    """
    View to for user to edit logs

    **Context**

    ``log``
        A single log related to the category.
    ``log_form``
    An instance of :form:`categories.LogForm`
    """
    if request.method == "POST":
        log = get_object_or_404(Log, pk=log_id)
        log_form = LogForm(data=request.POST, instance=log, prefix="edit")

        if log_form.is_valid() and log.user == request.user:
            log_form.save()
            messages.add_message(request, messages.SUCCESS, 'Log Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Log!')

    return HttpResponseRedirect(reverse('category_detail', args=[slug]))


@login_required
def log_delete(request, slug, log_id):
    """
    view to delete log
    """
    log = get_object_or_404(Log, pk=log_id)

    if log.user == request.user:
        log.delete()
        messages.add_message(request, messages.SUCCESS, 'Log deleted!')
    else:
        messages.add_message(request, messages.ERROR, "Deletion didn’t work, but you’ve still got control over your journey.")

    return HttpResponseRedirect(reverse('category_detail', args=[slug]))
