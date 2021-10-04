# Generated by Django 3.1.5 on 2021-02-01 15:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0015_category_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='time',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]