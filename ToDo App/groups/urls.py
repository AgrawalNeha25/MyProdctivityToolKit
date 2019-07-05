from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name="all"),
    path("new/", views.CreateGroup.as_view(), name="create"),
    path("posts/in/<int:pk>/",views.SingleGroup.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeleteGroup.as_view(),name="delete"),
    path("update/<int:pk>/",views.UpdateGroup.as_view(),name="update")
]
