# Generated by Django 4.2.7 on 2024-06-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0015_rename_rev_biblio_avales_biblio_rev_bilio'),
    ]

    operations = [
        migrations.AddField(
            model_name='avales_tuto',
            name='fecha',
            field=models.DateField(editable=True),
            preserve_default=False,
        ),
    ]