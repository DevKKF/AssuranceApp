# Generated by Django 3.2.15 on 2023-11-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0046_dossiersinistre_statut_pec'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossiersinistre',
            name='statut_prorogation',
            field=models.CharField(choices=[('ACCORDE', 'Accorde'), ('EN ATTENTE', 'Attente'), ('REJETE', 'Rejete')], default='EN ATTENTE', max_length=15, null=True),
        ),
    ]