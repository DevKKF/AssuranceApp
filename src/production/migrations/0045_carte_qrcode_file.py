# Generated by Django 3.2.15 on 2023-12-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0044_aliment_bureau'),
    ]

    operations = [
        migrations.AddField(
            model_name='carte',
            name='qrcode_file',
            field=models.ImageField(blank=True, null=True, upload_to='beneficiaire/cartes'),
        ),
    ]
