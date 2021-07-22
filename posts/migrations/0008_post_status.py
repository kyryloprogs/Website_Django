# Generated by Django 3.2.5 on 2021-07-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published'), ('R', 'Rejected')], default='D', max_length=2),
        ),
    ]