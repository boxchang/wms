# Generated by Django 3.0 on 2023-09-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0020_auto_20230908_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bin',
            field=models.ManyToManyField(to='stock.Bin'),
        ),
    ]
