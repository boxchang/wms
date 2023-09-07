# Generated by Django 3.0 on 2023-09-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20230907_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wo',
            name='item',
        ),
        migrations.AddField(
            model_name='wo',
            name='access_point',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wo',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='wo',
            name='item_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wo',
            name='lift',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='wo',
            name='shelf',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
