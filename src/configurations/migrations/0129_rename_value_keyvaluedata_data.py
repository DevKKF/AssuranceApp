# Generated by Django 4.0.3 on 2024-01-03 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0128_keyvaluedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyvaluedata',
            old_name='value',
            new_name='data',
        ),
    ]
