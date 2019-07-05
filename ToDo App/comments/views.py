from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from . import forms
from . import models

class CreateComment(LoginRequiredMixin, generic.CreateView):
    fields = ('message','files','post')
    model = models.Comment

class SingleComment(generic.DetailView):
    model = models.Comment

class DeleteComment(LoginRequiredMixin, generic.DeleteView):
    model = models.Comment
    success_url = reverse_lazy("posts:all")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Comment Deleted")
        return super().delete(*args, **kwargs)
