from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """
    Provides primary key type and configuration for the dashboard app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
