# Generated by Django 4.2.7 on 2023-11-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properites', '0006_record_remove_property_property_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='record',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]