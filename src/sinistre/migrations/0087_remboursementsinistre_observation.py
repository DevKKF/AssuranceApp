# Generated by Django 3.2.15 on 2024-04-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0086_alter_bordereauordonnancement_statut_paiement'),
    ]

    operations = [
        migrations.AddField(
            model_name='remboursementsinistre',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]