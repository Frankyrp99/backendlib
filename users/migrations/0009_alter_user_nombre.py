# Generated by Django 4.2.7 on 2024-07-07 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
