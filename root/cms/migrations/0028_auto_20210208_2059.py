# Generated by Django 2.2.7 on 2021-02-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0027_menu_templatedir'),
    ]

    operations = [
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.DeleteModel(
            name='templatedir',
        ),
    ]
