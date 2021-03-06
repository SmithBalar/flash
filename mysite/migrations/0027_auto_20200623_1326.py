# Generated by Django 3.0.3 on 2020-06-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0026_auto_20200623_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_thumbnail',
            field=models.ImageField(default='', upload_to='portfolio/images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default='', upload_to='review/images'),
        ),
    ]
