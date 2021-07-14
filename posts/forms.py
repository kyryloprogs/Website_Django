from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Post
        fields = ("title", "content")
