# Generated by Django 2.2 on 2020-04-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
