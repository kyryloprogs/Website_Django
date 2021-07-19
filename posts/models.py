from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # category = models.ForeignKey(Category,
    #                              on_delete=models.CASCADE,
    #                              null=True,
    #                              default=None,
    #                              related_name='posts')
    categories = models.ManyToManyField(Category, through='PostCategories')

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class PostCategories(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             null=True,
                             default=None,
                             related_name='post')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=None,
                                 related_name='category')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Post Categories'
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.post.title + " -> " + self.category.name
