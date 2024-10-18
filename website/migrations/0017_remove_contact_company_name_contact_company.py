# Generated by Django 5.1.1 on 2024-10-18 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='company_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_set', to='website.account'),
        ),
    ]
