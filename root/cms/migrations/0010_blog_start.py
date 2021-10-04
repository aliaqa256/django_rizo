# Generated by Django 3.1.5 on 2021-01-26 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0009_auto_20210125_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='start',
            field=models.ManyToManyField(blank=True, related_name='like_star', to=settings.AUTH_USER_MODEL),
        ),
    ]