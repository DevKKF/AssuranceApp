# Generated by Django 3.2.15 on 2023-12-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0039_auto_20231124_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='code_provisoire',
            field=models.CharField(max_length=25, null=True),
        ),
    ]