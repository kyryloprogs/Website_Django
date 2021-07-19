from django import forms
from django.forms import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        min_length=2
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={"class": "form-control"}),
        min_length=2
    )

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 5:
            raise ValidationError('Err')
        return title

    class Meta:
        model = Post
        fields = ("title", "content")
