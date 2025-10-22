from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    """
    Provides primary key type and configuration for the categories app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories'
