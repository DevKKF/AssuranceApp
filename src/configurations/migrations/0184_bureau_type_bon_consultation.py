# Generated by Django 3.2.15 on 2024-06-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0183_merge_0177_merge_20240531_1446_0182_alimentbaobab'),
    ]

    operations = [
        migrations.AddField(
            model_name='bureau',
            name='type_bon_consultation',
            field=models.CharField(choices=[('AUTO CARBONE', 'Auto Carbone'), ('NUMERIQUE', 'Numerique')], default='AUTO CARBONE', max_length=15, null=True),
        ),
    ]
