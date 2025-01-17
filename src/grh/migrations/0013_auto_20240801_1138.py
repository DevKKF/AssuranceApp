# Generated by Django 3.2.15 on 2024-08-01 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0110_merge_20240726_1026'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grh', '0012_enrolementappmobile_enrolementprospect'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampagneAppmobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('statut', models.CharField(choices=[('VALIDE', 'Valide'), ('SUPPRIME', 'Supprime'), ('BROUILLON', 'Brouillon'), ('CLOTURE', 'Cloture')], max_length=15, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('formulegarantie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.formulegarantie')),
                ('police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='production.police')),
            ],
            options={
                'verbose_name': 'Campagne_appmobile',
                'verbose_name_plural': 'campagne_appmobile',
                'db_table': 'campagne_appmobile',
            },
        ),
        migrations.CreateModel(
            name='CampagneAppmobileProspect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('statut_enrolement', models.CharField(choices=[('EN ATTENTE', 'Attente'), ('EN COURS', 'Encours'), ('SOUMIS', 'Soumis'), ('VALIDE', 'Valide'), ('REJETE', 'Rejete'), ('INCORPORE', 'Incorpore')], default='EN ATTENTE', max_length=15, null=True)),
                ('campagne_appmobile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='grh.campagneappmobile')),
                ('mouvement', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='production.mouvement')),
                ('prospect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='grh.prospect')),
                ('uiid', models.CharField(max_length=255, blank=False, null=True)),
                ('lien', models.CharField(max_length=64, blank=False, null=True))
            ],
        ),
        migrations.RemoveField(
            model_name='enrolementprospect',
            name='enrolement',
        ),
        migrations.RemoveField(
            model_name='enrolementprospect',
            name='prospect',
        ),
        migrations.DeleteModel(
            name='EnrolementAppMobile',
        ),
        migrations.DeleteModel(
            name='EnrolementProspect',
        ),
    ]
