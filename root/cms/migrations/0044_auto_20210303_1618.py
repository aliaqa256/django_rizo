# Generated by Django 3.1.6 on 2021-03-03 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0043_auto_20210303_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pwsrest',
            name='datatime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
