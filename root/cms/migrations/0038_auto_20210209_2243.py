# Generated by Django 3.1.6 on 2021-02-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0037_chanel_title2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='mozoee',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
