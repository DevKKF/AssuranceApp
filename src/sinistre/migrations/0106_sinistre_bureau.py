# Generated by Django 3.2.15 on 2024-05-24 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0172_changementformule_sousregroupementacte_sousregroupementacteacte'),
        ('sinistre', '0105_auto_20240524_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='bureau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.bureau'),
        ),
    ]