# Generated by Django 3.1.5 on 2021-01-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='my_tags',
            field=models.ManyToManyField(blank=True, to='cms.Tag'),
        ),
    ]
