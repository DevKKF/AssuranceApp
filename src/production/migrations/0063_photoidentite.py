# Generated by Django 3.2.15 on 2024-01-18 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0062_mouvementaliment_police'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoIdentite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('aliment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='production.aliment')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'db_table': 'photo',
            },
        ),
    ]