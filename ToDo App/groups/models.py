from django.db import models
from django.conf import settings
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["name"]
