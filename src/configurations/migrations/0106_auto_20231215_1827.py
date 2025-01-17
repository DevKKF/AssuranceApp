# Generated by Django 3.2.15 on 2023-12-15 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0105_auto_20231214_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='compagnieveos',
            name='COM_APPORT_COMPTANT',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compagnieveos',
            name='COM_APPORT_TERME',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compagnieveos',
            name='COM_GESTION',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescripteur',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau'),
        ),
        migrations.CreateModel(
            name='ParamActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delais_controle', models.IntegerField(blank=True, null=True)),
                ('option_seance', models.BooleanField(default=False)),
                ('option_quantite', models.BooleanField(default=False)),
                ('accord_automatique', models.BooleanField(default=False)),
                ('specialiste_uniquement', models.BooleanField(default=False)),
                ('est_gratuit', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('acte', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configurations.acte')),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau')),
            ],
            options={
                'verbose_name': "Paramétrage de l'acte",
                'verbose_name_plural': "Paramétrages de l'acte",
                'db_table': 'param_actes',
            },
        ),
    ]
