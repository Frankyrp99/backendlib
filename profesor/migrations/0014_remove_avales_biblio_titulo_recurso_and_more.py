# Generated by Django 4.2.7 on 2024-06-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0013_avales_biblio_niv_act'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avales_biblio',
            name='titulo_recurso',
        ),
        migrations.AddField(
            model_name='avales_biblio',
            name='total_asient',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
