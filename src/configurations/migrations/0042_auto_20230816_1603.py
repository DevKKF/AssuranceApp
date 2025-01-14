# Generated by Django 3.2.15 on 2023-08-16 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0041_actesousrubrique_sousacte_sousrubrique'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupementActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': "Groupement d'acte",
                'verbose_name_plural': "Groupements d'actes",
                'db_table': 'groupement_acte',
            },
        ),
        migrations.CreateModel(
            name='SousRubriqueGroupementActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.BooleanField(default=True)),
                ('groupement_acte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.groupementacte')),
                ('sous_rubrique', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='configurations.sousrubrique')),
            ],
            options={
                'verbose_name': 'Contenu de la sous-rubrique',
                'verbose_name_plural': 'Contenus de la sous-rubrique',
                'db_table': 'sous_rubrique_groupement_acte',
            },
        ),
        migrations.RemoveField(
            model_name='sousacte',
            name='acte',
        ),
        migrations.DeleteModel(
            name='ActeSousRubrique',
        ),
        migrations.DeleteModel(
            name='SousActe',
        ),
        migrations.AddField(
            model_name='acte',
            name='groupement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.groupementacte'),
        ),
    ]
