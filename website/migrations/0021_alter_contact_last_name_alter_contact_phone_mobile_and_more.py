# Generated by Django 5.1.1 on 2024-10-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_remove_contact_contract_expiry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_office',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
