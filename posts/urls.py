from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import MyView


app_name = "posts"

urlpatterns = [
    path("posts/", cache_page(42, cache='db_cache'), views.index, name="index"),
    path("add/", views.MyView.as_view(), name="add_post"),
    path("<int:post_id>/", views.PostDetailView.as_view(), name="details"),
    path("login/", views.login_view, name="login_view")
]
