# Generated by Django 3.0.2 on 2020-01-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reputation',
            field=models.IntegerField(null=True),
        ),
    ]
