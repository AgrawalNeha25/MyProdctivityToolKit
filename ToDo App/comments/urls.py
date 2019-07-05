from django.urls import path
from . import views

app_name='comments'

urlpatterns = [
    path("new/", views.CreateComment.as_view(), name="create"),
    path("by/<int:pk>/",views.SingleComment.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeleteComment.as_view(),name="delete"),
]
