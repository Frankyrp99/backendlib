# Generated by Django 4.2.7 on 2024-07-04 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0019_profesor_apellidos_autor_profesor_departamento_autor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='apellidos_autor',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='departamento_autor',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='nombre_autor',
        ),
    ]
