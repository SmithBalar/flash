# Generated by Django 3.0.3 on 2020-06-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0029_auto_20200623_1435'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.FileField(default='', upload_to='review/images'),
        ),
    ]
