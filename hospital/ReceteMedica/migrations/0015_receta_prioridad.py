# Generated by Django 4.2.2 on 2024-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceteMedica', '0014_receta_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='prioridad',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
