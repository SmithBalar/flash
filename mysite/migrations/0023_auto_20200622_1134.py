# Generated by Django 3.0.3 on 2020-06-22 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_auto_20200622_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='ser_desc',
            new_name='service_desc',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='ser_name',
            new_name='service_name',
        ),
    ]
