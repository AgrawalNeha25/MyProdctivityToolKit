from django.db import models
from django.conf import settings
from django.urls import reverse


from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    name = models.CharField(max_length = 256)
    status = models.CharField(max_length = 256, null=True)
    deadline = models.CharField(max_length = 256, null=True)
    priority = models.IntegerField()
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username,"pk": self.pk})

    class Meta:
        ordering = ["priority"]
        unique_together = ["user", "name"]
