# Generated by Django 3.2.19 on 2023-07-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0008_auto_20230712_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulegarantie',
            name='code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]