# Generated by Django 4.2.7 on 2024-07-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0023_avales_biblio_autor_avales_tuto_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='e_issn',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='isbn',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='issn',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]