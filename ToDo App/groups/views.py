from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from groups.models import Group
from . import models

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class DeleteGroup(generic.DeleteView):
    model = Group
    success_url = reverse_lazy("groups:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Project Deleted")
        return super().delete(*args, **kwargs)

class UpdateGroup(generic.UpdateView):
    fields = ("name", "description")
    model = Group
