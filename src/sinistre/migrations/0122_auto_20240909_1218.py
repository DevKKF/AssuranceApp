# Generated by Django 3.2.15 on 2024-09-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0121_auto_20240904_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinistre',
            name='montant_refacture_client',
            field=models.DecimalField(decimal_places=17, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='sinistre',
            name='montant_refacture_compagnie',
            field=models.DecimalField(decimal_places=17, max_digits=50, null=True),
        ),
    ]
