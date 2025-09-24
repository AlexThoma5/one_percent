from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Stores a single category
    """
    name = models.CharField(max_length=200, unique=True)
    icon = models.CharField(max_length=200, default='fa-regular fa-pen-to-square')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
