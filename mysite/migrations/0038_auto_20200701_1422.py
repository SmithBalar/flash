# Generated by Django 3.0.3 on 2020-07-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0037_auto_20200701_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='map_url',
            field=models.TextField(blank=True, max_length='1500'),
        ),
    ]
