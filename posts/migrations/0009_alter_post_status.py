# Generated by Django 3.2.5 on 2021-07-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published'), ('R', 'Rejected')], default='P', max_length=2),
        ),
    ]
