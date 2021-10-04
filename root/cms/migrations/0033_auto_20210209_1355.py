# Generated by Django 3.1.6 on 2021-02-09 10:25

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0032_merge_20210209_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketmain',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='ticketmain',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='ticketmain',
            name='sender',
        ),
        migrations.AlterField(
            model_name='templatedir',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='cms/templates/page/'), upload_to=''),
        ),
        migrations.DeleteModel(
            name='TicketAnswer',
        ),
        migrations.DeleteModel(
            name='TicketMain',
        ),
        migrations.DeleteModel(
            name='TicketSend',
        ),
    ]
