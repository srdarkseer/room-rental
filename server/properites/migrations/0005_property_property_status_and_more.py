# Generated by Django 4.2.7 on 2023-11-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properites', '0004_property_property_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_status',
            field=models.ManyToManyField(to='properites.propertystatus'),
        ),
        migrations.AlterField(
            model_name='propertystatus',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertystatus',
            name='start_date',
            field=models.DateField(),
        ),
    ]
