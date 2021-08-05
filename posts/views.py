from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView

from django import forms
from .models import Post, PostManager
from .forms import PostForm
from django.urls import reverse
from django.utils.translation
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import caches


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


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/index.html"
    queryset = Post.objects.published()

    login_url = 'login/'


class PostDetailView(ListView):
    model = Post
    context_object_name = "post"
    template_name = "posts/details.html"


# @login_required(login_url='/login')
# @permission_required(['posts.view_post'])
@cache_page(60, cache='db_cache')
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login/')
    posts = Post.objects.all()
    # if not request.user.has_perm('posts.view_post'):
    #     redirect('posts/index.html')
    context = {"posts": posts}
    db_cache = caches['db_cache']
    if not posts:
        post_qs = Post.objects.select_related('category').prefetch_related('post_categories',
                                                                           'post_categories__category')
        db_cache.set('posts_list', post_qs, 240)
    # from django.contrib.auth.models import User
    # user = User.objects.create_user('username', 'email', 'password')

   # user.set_password("user")
    return render(request, "posts/index.html", context)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm_password']

        if password != confirm:
            raise forms.ValidationError('Passwords not equal')

        return self.cleaned_data


def login_view(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            if user.is_active:
                login(request, user)

    else:

        form = LoginForm()

    return render(request, 'posts/index.html', {'form': form})


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


# request.session['user_id'] = 42
# request.session['user_data'] = {
#                    'posts': 32
# }
# del request.session['user_id']
# request.session.modified = true
# request.session.flush()
