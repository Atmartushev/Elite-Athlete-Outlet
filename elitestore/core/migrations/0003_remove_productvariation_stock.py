# Generated by Django 5.0.3 on 2024-05-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_productvariation_price_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='stock',
        ),
    ]
