# Generated by Django 3.0.8 on 2020-07-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200716_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='thumbnail',
        ),
    ]