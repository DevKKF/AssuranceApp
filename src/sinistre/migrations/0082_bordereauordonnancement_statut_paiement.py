# Generated by Django 3.2.15 on 2024-03-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0081_sinistre_statut_paiement'),
    ]

    operations = [
        migrations.AddField(
            model_name='bordereauordonnancement',
            name='statut_paiement',
            field=models.CharField(choices=[('EN ATTENTE', 'Attente'), ('ORDONNANCE', 'Ordonnance'), ('PAYE', 'Paye')], default='EN ATTENTE', max_length=15, null=True),
        ),
    ]
