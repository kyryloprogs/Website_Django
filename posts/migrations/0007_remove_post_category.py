# Generated by Django 3.2.5 on 2021-07-19 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_migrate_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
