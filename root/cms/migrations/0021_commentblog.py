# Generated by Django 3.1.5 on 2021-02-07 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0020_auto_20210203_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cms.blog')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
