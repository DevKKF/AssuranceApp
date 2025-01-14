# Generated by Django 3.2.15 on 2024-01-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0057_merge_0056_auto_20240109_1128_0056_mouvementaliment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouvement',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='mouvement',
            name='libelle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
