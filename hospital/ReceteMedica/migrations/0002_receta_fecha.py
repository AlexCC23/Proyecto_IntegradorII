# Generated by Django 4.2.2 on 2024-04-13 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ReceteMedica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
