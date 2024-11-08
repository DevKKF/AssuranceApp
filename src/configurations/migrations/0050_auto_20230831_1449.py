# Generated by Django 3.2.15 on 2023-08-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0049_auto_20230831_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarif',
            name='coef_classique',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='coef_mutuelle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='coef_public_chu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='coef_public_hg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='coef_public_ica',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='cout_classique',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='cout_mutuelle',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='cout_public_chu',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='cout_public_hg',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='cout_public_ica',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='lettre_cle_classique',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='lettre_cle_mutuelle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='lettre_cle_public_chu',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='lettre_cle_public_hg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='lettre_cle_public_ica',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='pu_classique',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='pu_mutuelle',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='pu_public_chu',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='pu_public_hg',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarif',
            name='pu_public_ica',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COEF_CLASSIQUE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COEF_MUTUELLE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COEF_PUBLIC_CHU',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COEF_PUBLIC_HG',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COEF_PUBLIC_ICA',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COUT_CLASSIQUE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COUT_MUTUELLE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COUT_PUBLIC_CHU',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COUT_PUBLIC_HG',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='COUT_PUBLIC_ICA',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='LETTRE_CLE_CLASSIQUE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='LETTRE_CLE_MUTUELLE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='LETTRE_CLE_PUBLIC_HG',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='LETTRE_PUBLIC_CHU',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='LETTRE_PUBLIC_ICA',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='PU_CLASSIQUE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='PU_MUTUELLE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='PU_PUBLIC_CHU',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='PU_PUBLIC_HG',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tarifexcel',
            name='PU_PUBLIC_ICA',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
