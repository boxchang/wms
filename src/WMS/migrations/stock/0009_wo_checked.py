# Generated by Django 3.0 on 2023-09-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_auto_20230831_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='wo',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
