# Generated by Django 4.2.2 on 2024-06-10 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0004_rename_firma_didigtal_pedido_firma_digtal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='firma_digtal',
            new_name='firma_digital',
        ),
    ]
