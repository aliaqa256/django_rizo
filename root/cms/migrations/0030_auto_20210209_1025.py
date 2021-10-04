# Generated by Django 3.1.6 on 2021-02-09 06:55

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_menu_templatedir'),
    ]

    operations = [
        migrations.CreateModel(
            name='staticdir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=250, unique=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='template'), upload_to='static/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'staticdir',
                'verbose_name_plural': 'staticdir',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='templatedir',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='template'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='templatedir',
            name='token',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
