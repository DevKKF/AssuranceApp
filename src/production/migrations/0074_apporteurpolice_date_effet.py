# Generated by Django 3.2.15 on 2024-02-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0073_auto_20240205_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='apporteurpolice',
            name='date_effet',
            field=models.DateField(blank=True, null=True),
        ),
    ]
