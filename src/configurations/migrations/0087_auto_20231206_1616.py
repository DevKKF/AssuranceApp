# Generated by Django 3.2.15 on 2023-12-06 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0086_merge_0083_affection_code_0085_prescripteurveos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestataireveos',
            options={'verbose_name': 'Prestataire Veos', 'verbose_name_plural': 'Prestataires VEOS'},
        ),
        migrations.AlterField(
            model_name='alimentveos',
            name='STATUT_IMPORT',
            field=models.BooleanField(default=False),
        ),
    ]
