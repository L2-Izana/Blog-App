# Generated by Django 5.0.1 on 2024-03-04 12:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_react_timestamp'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LastestReact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(blank=True, choices=[('Like', 'Like'), ('Love', 'Love'), ('Haha', 'Haha'), ('Wow', 'Wow'), ('Sad', 'Sad'), ('Angry', 'Angry')], max_length=6, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
