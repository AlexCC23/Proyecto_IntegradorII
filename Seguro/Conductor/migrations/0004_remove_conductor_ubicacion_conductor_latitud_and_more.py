# Generated by Django 4.2.2 on 2024-06-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conductor', '0003_alter_conductor_dni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductor',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='conductor',
            name='Latitud',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='conductor',
            name='Longitud',
            field=models.CharField(max_length=200, null=True),
        ),
    ]