# Generated by Django 4.2.7 on 2023-11-30 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='gello', max_length=255),
            preserve_default=False,
        ),
    ]