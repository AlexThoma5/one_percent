from django.contrib import admin
from .models import Category, Log

# Register your models here.
admin.site.register(Category)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "created_on")
    search_fields = ("title",)
    list_filter = ("category", "created_on")
