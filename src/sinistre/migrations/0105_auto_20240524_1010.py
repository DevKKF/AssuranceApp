# Generated by Django 3.2.15 on 2024-05-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0104_alter_sinistre_date_paiement'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='depassement_accepte',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='frais_reel_accepte',
            field=models.DecimalField(decimal_places=17, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='part_assure_accepte',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='part_compagnie_accepte',
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
    ]
