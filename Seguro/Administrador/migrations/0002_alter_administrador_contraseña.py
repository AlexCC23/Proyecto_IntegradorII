# Generated by Django 4.2.2 on 2024-04-15 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='contraseña',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
