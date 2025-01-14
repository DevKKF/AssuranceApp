# Generated by Django 3.2.15 on 2024-02-10 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0151_apporteurveos_cd_pays'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteTresorerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Compte de trésorerie',
                'verbose_name_plural': 'Comptes de trésorerie',
                'db_table': 'compte_tresorerie',
            },
        ),
        migrations.AddField(
            model_name='banque',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau'),
        ),
        migrations.AddField(
            model_name='banque',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banque',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
