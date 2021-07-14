from django.urls import path

from . import views


app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_post, name="add_post"),
    path("<int:post_id>/", views.details, name="details"),
]
