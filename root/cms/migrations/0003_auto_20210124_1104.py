# Generated by Django 3.1.5 on 2021-01-24 11:04

import cms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cms.models.upload_image_path),
        ),
    ]
