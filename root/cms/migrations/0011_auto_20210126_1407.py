# Generated by Django 3.1.5 on 2021-01-26 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_blog_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='start',
            new_name='star',
        ),
    ]
