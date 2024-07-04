# Generated by Django 4.2.7 on 2024-07-04 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0020_remove_profesor_apellidos_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profesores', to='profesor.autor'),
            preserve_default=False,
        ),
    ]