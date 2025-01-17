# Generated by Django 3.2.15 on 2024-07-03 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0197_tarif_deleted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='paramacte',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pa_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paramacte',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pa_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
