# Generated by Django 3.2.15 on 2024-05-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0172_changementformule_sousregroupementacte_sousregroupementacteacte'),
    ]

    operations = [
        migrations.AddField(
            model_name='compagnie',
            name='has_taux_multiple',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paramproduitcompagnie',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]