# Generated by Django 4.2.7 on 2023-12-02 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_actice_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nombre',
            new_name='name',
        ),
    ]
