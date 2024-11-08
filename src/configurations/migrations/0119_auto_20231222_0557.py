# Generated by Django 3.2.15 on 2023-12-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0118_tarif_validated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestataire',
            name='has_tarif_prestataire',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='statut_validite',
            field=models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon')], default='VALIDE', max_length=15, null=True),
        ),
    ]