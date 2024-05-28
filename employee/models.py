from django.db import models

from utils.models import BaseModel


class Employee(BaseModel):
    id = models.UUIDField(editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    image_url = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
