from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    Stores a single category
    """
    name = models.CharField(max_length=200, unique=True)
    icon = models.CharField(max_length=200,
                            default='fa-regular fa-pen-to-square')
    slug = models.SlugField(max_length=200, unique=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Log(models.Model):
    """
    Stores a single log entry related to :model:`auth.user`
    and :model:`categories.Category`
    """
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)  # Optional field for extra notes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name="logs")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.title} ({self.category}) made by {self.user}'
