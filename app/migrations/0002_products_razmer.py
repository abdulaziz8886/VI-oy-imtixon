# Generated by Django 5.1.5 on 2025-01-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='razmer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
