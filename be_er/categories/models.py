# categories/models.py
from django.db import models
from core.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
