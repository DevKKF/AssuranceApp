# Generated by Django 4.0.3 on 2024-01-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0127_apporteur_bureau'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValueData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('statut', models.BooleanField(default=True)),
                ('value', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date mise à jour')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
                'db_table': 'keyvaluedata',
            },
        ),
    ]
