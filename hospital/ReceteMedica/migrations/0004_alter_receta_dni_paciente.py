# Generated by Django 4.2.2 on 2024-04-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceteMedica', '0003_alter_receta_dni_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='dni_Paciente',
            field=models.CharField(max_length=10),
        ),
    ]