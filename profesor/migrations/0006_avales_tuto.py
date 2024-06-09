# Generated by Django 4.2.7 on 2024-05-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0005_profesor_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='avales_tuto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('titulo_recurso', models.CharField(max_length=500)),
                ('departamento', models.CharField(blank=True, max_length=200)),
                ('tomo', models.CharField(blank=True, max_length=50)),
                ('folio', models.CharField(blank=True, max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
