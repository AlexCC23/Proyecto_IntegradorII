# Generated by Django 4.2.2 on 2024-04-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicina', '0002_remove_medicina_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicina',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
