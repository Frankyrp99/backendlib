# Generated by Django 4.2.7 on 2024-03-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0002_remove_profesor_cd_rom_remove_profesor_ci_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]