# Generated by Django 3.2.15 on 2023-12-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0048_auto_20231225_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quittance',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
