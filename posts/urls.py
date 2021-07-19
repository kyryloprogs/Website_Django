from django.urls import path

from . import views
from .views import MyView


app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("add/", views.MyView.as_view(), name="add_post"),
    path("<int:post_id>/", views.PostDetailView.as_view(), name="details"),
]
