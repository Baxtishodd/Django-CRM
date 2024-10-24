# Generated by Django 5.1.1 on 2024-10-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_alter_product_quantity_in_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='products',
            field=models.ManyToManyField(related_name='deals', to='website.product'),
        ),
    ]