# Generated by Django 3.2.15 on 2024-04-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0092_auto_20240409_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='montant_base_remboursement',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='montant_remboursement_accepte',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='montant_remboursement_refuse',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='motif_refus_remboursement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]