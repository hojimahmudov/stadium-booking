# Generated by Django 5.0.4 on 2024-05-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(to='User.permission'),
        ),
    ]
