# Generated by Django 3.1.5 on 2021-02-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0039_blog_short_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturls',
            name='short',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]