# Generated by Django 3.2.15 on 2023-08-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0021_merge_20230808_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='apporteur',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('', 'Choisir')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='mode_renouvellement',
            field=models.CharField(choices=[('TACITE RECONDUCTION', 'Tacite Reconduction'), ('SANS TACITE RECONDUCTION', 'Sans Tacite Reconduction'), ('', 'Choisir')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='participation',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('', 'Choisir')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='placement_gestion',
            field=models.CharField(choices=[('LOCAL', 'En Local'), ('PAR LE COURTIER MASTER', 'Par Le Courtier Master'), ('', 'Choisir')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='preavis_de_resiliation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='police',
            name='programme_international',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non'), ('', 'Choisir')], max_length=3, null=True),
        ),
    ]