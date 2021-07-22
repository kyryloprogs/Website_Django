from django import forms
from django.forms import ValidationError
from .models import Post, Category
from django.forms import (
    modelform_factory,
    formset_factory,
    modelformset_factory
)

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
    status = forms.ChoiceField(choices=Post.STATUS,
                               label="Status")

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Err')
        return title

    class Meta:
        model = Post
        fields = ("title", "content", "status", "categories")
