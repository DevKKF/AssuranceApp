# Generated by Django 3.2.15 on 2023-10-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0067_periodecomptable_typeremboursement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodecomptable',
            name='code',
        ),
        migrations.AddField(
            model_name='periodecomptable',
            name='annee',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='periodecomptable',
            name='mois',
            field=models.IntegerField(null=True),
        ),
    ]
