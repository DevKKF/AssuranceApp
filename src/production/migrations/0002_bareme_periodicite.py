# Generated by Django 3.2.19 on 2023-06-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0005_periodicite'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bareme',
            name='periodicite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.periodicite'),
        ),
    ]