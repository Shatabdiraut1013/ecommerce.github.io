# Generated by Django 3.0.8 on 2020-07-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200715_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default='', max_length=20),
        ),
    ]