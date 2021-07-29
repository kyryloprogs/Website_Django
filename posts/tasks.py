from celery import shared_task
from django.db.models import Count

from posts.models import Post


@shared_task
def report():
    rep = list(Post.objects.values('status')
               .annotate(count=Count('status')))
    return rep
