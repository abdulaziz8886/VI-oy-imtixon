# Generated by Django 5.1.5 on 2025-01-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_zay_first_category_month_img_catagorys_of_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagorys_of_month',
            name='imgs',
        ),
    ]
