# Generated by Django 2.2 on 2020-04-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]