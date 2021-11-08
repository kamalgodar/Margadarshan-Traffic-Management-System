# Generated by Django 3.0.2 on 2020-01-25 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20200125_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='validate',
            field=models.ManyToManyField(blank=True, related_name='validate', to=settings.AUTH_USER_MODEL),
        ),
    ]
