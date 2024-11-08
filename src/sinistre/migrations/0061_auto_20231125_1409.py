# Generated by Django 3.2.15 on 2023-11-25 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinistre', '0060_dossiersinistre_date_survenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinistre',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='sinistre',
            name='deleted_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='deleted_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
