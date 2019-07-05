from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ("message","files","post")
        model = models.Comment

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["post"].queryset = (
                models.Post.objects.filter(
                    pk__in=user.posts.values_list("post__pk")
                )
            )
