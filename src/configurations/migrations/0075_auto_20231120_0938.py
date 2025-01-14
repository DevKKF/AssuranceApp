# Generated by Django 3.2.15 on 2023-11-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0074_typeremboursement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='typepriseencharge',
            name='statut_selectable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='acte',
            name='code',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
    ]
