# Generated by Django 4.2.7 on 2024-03-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0003_alter_profesor_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='titulo_recurso',
            field=models.CharField(max_length=500),
        ),
    ]
