from django.db import models
from django.conf import settings
from django.urls import reverse


from posts.models import Post

class Comment(models.Model):
    message = models.CharField(max_length = 256, null=True)
    files = models.FileField(upload_to='comments/files',blank=True, null=True)
    post = models.ForeignKey(Post, related_name="comments",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("comments:single", kwargs={"pk": self.pk})
