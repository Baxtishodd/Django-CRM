# Generated by Django 5.1.1 on 2024-10-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_contact_company_name_contact_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]