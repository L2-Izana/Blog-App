# Generated by Django 5.0.1 on 2024-03-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='curr_place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='curr_work',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='highest_education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='relationship',
            field=models.CharField(blank=True, choices=[('S', 'Single'), ('D', 'Dating'), ('M', 'Married'), ('P', 'Private')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]