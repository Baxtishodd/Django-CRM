# Generated by Django 5.1.1 on 2024-10-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_product_product_picture_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_in_stock',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]