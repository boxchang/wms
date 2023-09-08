# Generated by Django 3.0 on 2023-09-07 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_wo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wo',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='wo',
            name='item_code',
        ),
        migrations.AddField(
            model_name='wo',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wo_item', to='stock.Item'),
            preserve_default=False,
        ),
    ]