# Generated by Django 4.2.2 on 2024-04-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
