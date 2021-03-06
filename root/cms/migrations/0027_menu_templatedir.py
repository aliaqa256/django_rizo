# Generated by Django 2.2.7 on 2021-02-08 17:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_remove_commentblog_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='templatedir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(unique=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='template'), upload_to='template/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'templatedir',
                'verbose_name_plural': 'templatedirs',
            },
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=250)),
                ('file', models.ManyToManyField(blank=True, related_name='file_template', to='cms.templatedir')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
            },
        ),
    ]
