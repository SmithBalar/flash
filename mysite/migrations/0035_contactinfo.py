# Generated by Django 3.0.3 on 2020-07-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0034_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_address', models.TextField()),
                ('website', models.URLField()),
                ('map_url', models.URLField(blank=True)),
            ],
        ),
    ]
