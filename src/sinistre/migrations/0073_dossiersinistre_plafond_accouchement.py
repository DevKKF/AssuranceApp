# Generated by Django 3.2.15 on 2024-01-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0072_alter_sinistre_aliment'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='plafond_accouchement',
            field=models.FloatField(null=True),
        ),
    ]