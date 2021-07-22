from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .models import Post, PostManager
from .forms import PostForm
from django.urls import reverse


class MyView(View):

    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {"form": form}
        return render(request, "posts/add_post.html", context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:index'))  # HttpResponseRedirect('/posts/')
        context = {"form": form}
        return render(request, "posts/add_post.html", context)


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/index.html"
    queryset = Post.objects.published()


class PostDetailView(ListView):
    model = Post
    context_object_name = "post"
    template_name = "posts/details.html"


def index(request):
    context = {"posts": Post.objects.all()}
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

# def add_post(request):
#     form = PostForm()
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("posts:index")
#     context = {"form": form}
#     return render(request, "posts/add_post.html", context)
