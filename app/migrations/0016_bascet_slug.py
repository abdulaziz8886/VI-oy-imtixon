# Generated by Django 5.1.5 on 2025-01-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_bascet_jami'),
    ]

    operations = [
        migrations.AddField(
            model_name='bascet',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
