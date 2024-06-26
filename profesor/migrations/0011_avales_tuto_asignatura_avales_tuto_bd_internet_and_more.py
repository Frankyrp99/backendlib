# Generated by Django 4.2.7 on 2024-06-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0010_delete_avalunificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='avales_tuto',
            name='asignatura',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='bd_internet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='bd_local',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='biblio_personal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='busqueda_internet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='cd_rom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='curso_pos',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='curso_pos_bus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='disciplina',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='doctorado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='evaluacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='maestria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='no_biblio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='otros',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='pag',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='project_cur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='projecto',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='trabajo_diploma',
            field=models.BooleanField(default=False),
        ),
    ]
