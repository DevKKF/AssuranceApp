# Generated by Django 3.2.15 on 2023-12-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0045_carte_qrcode_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliment',
            name='apci_ald',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]