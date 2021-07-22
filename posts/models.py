from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem



class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Post.STATUS_PUBLISHED)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'categories'


class Post(models.Model):
    STATUS_DRAFT = "D"
    STATUS_PUBLISHED = "P"
    STATUS_REJECTED = "R"
    STATUS = (
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
        (STATUS_REJECTED, "Rejected")
    )
    objects = PostManager()
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
    status = models.CharField(choices=STATUS, default=STATUS_DRAFT, max_length=2)
    tags = GenericRelation(TaggedItem)

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
