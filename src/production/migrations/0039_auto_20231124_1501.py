# Generated by Django 3.2.15 on 2023-11-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0038_document_fichier'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='code_provisoire',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(max_length=25, null=True),
        ),
    ]