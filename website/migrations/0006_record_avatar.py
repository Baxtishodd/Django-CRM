# Generated by Django 5.1.1 on 2024-09-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_product_date_of_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]