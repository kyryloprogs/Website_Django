from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    name = models.CharField(max_length=100)


class TaggedItem(models.Model):
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')