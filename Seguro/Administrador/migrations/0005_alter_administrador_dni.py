# Generated by Django 5.0.4 on 2024-04-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_alter_administrador_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='dni',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
