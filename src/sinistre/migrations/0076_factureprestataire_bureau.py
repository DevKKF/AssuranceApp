# Generated by Django 3.2.15 on 2024-01-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0137_merge_20240123_0827'),
        ('sinistre', '0075_factureprestataire_type_remboursement'),
    ]

    operations = [
        migrations.AddField(
            model_name='factureprestataire',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau'),
        ),
    ]
