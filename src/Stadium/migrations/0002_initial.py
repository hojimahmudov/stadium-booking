# Generated by Django 5.0.4 on 2024-04-30 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Stadium', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stadiumimage',
            name='stadium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stadium.stadium'),
        ),
    ]
