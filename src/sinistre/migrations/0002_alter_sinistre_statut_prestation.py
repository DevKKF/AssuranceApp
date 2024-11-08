# Generated by Django 3.2.19 on 2023-06-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinistre',
            name='statut_prestation',
            field=models.CharField(choices=[('EFFECTUE', 'Effectue'), ('NON EFFECTUE', 'Attente')], default='NON EFFECTUE', max_length=15, null=True),
        ),
    ]
