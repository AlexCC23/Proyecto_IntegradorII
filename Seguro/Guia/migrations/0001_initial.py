# Generated by Django 4.2.2 on 2024-07-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.CharField(max_length=9)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]