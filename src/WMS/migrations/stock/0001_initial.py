# Generated by Django 3.0 on 2023-08-30 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage_Type',
            fields=[
                ('type_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='storage_type_create_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_addr', models.CharField(blank=True, max_length=15, null=True)),
                ('lift', models.CharField(blank=True, max_length=1, null=True)),
                ('access_point', models.CharField(blank=True, max_length=1, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('enable', models.BooleanField(default=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='storage_create_by', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='storage_type', to='stock.Storage_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='location_create_by', to=settings.AUTH_USER_MODEL)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='storage_location', to='stock.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('bin_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bin_create_by', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='location_bin', to='stock.Location')),
            ],
        ),
    ]