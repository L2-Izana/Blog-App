# Generated by Django 5.0.1 on 2024-02-26 15:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='react',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
