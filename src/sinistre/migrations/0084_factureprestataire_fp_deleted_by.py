# Generated by Django 3.2.15 on 2024-03-19 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinistre', '0083_merge_20240308_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='factureprestataire',
            name='fp_deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='fp_deleted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
