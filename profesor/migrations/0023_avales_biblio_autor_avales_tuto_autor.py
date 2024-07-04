# Generated by Django 4.2.7 on 2024-07-04 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0022_alter_profesor_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='avales_biblio',
            name='autor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bibliografias', to='profesor.autor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='avales_tuto',
            name='autor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tutorias', to='profesor.autor'),
            preserve_default=False,
        ),
    ]