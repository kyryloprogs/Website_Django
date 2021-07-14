from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


def index(request):
    context = {"posts": Post.objects.select_related('category')}
    return render(request, "posts/index.html", context)


def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.save()
            return redirect("posts:index")
    context = {"post": post, "form": form}
    return render(request, "posts/details.html", context)


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:index")
    context = {"form": form}
    return render(request, "posts/add_post.html", context)
