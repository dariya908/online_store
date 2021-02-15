# Generated by Django 3.1.5 on 2021-02-10 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210208_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=datetime.date(2021, 2, 10)),
        ),
    ]