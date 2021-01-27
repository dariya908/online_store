# Generated by Django 3.1.5 on 2021-01-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]