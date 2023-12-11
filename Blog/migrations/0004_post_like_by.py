# Generated by Django 4.2.6 on 2023-11-07 07:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0003_post_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_by',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
