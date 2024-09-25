# Generated by Django 5.1.1 on 2024-09-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_record_birthday_record_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='father_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='family_situation',
            field=models.CharField(choices=[("Yolg'iz", "Yolg'iz"), ('Oilali', 'Oilali')], default="Yolg'iz", max_length=10),
        ),
    ]
