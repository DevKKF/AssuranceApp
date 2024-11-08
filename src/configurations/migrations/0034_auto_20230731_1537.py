# Generated by Django 3.2.15 on 2023-07-31 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0033_sinistreveos_num_compagnie'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeActe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': "Type d'acte",
                'verbose_name_plural': "Types d'acte",
                'db_table': 'type_actes',
            },
        ),
        migrations.AddField(
            model_name='acte',
            name='type_acte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.typeacte'),
        ),
    ]
