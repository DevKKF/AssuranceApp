# Generated by Django 3.2.15 on 2024-03-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0082_auto_20240305_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliment',
            name='statut_incorporation',
            field=models.CharField(choices=[('ENCOURS', 'Encours'), ('INCORPORE', 'Incorpore')], default='INCORPORE', max_length=15, null=True),
        ),
    ]
