# Generated by Django 3.2.15 on 2024-09-09 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0119_merge_20240909_1413'),
        ('sinistre', '0121_auto_20240904_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='factureprestataire',
            name='assure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.client'),
        ),
    ]
