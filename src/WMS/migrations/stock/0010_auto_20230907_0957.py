# Generated by Django 3.0 on 2023-09-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_wo_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wo',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(max_length=10),
        ),
    ]