from django.contrib import admin

from .models import Post, Category, PostCategories


class PostCategoryInline(admin.TabularInline):
    model = PostCategories


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'created_at')
    inlines = [
        PostCategoryInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
