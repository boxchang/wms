from django.db import models
from django.conf import settings


class Storage_Type(models.Model):
    type_code = models.CharField(max_length=6, primary_key=True)
    type_name = models.CharField(max_length=50, blank=False, null=False)
    update_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                  related_name='storage_type_create_by')

    def __str__(self):
        return self.type_name


class Storage(models.Model):
    storage_code = models.CharField(max_length=6, primary_key=True)
    type = models.ForeignKey(Storage_Type, related_name='storage_type', on_delete=models.DO_NOTHING)
    desc = models.CharField(max_length=200, blank=True, null=True)
    ip_addr = models.CharField(max_length=15, blank=True, null=True)
    lift = models.CharField(max_length=1, blank=True, null=True)
    access_point = models.CharField(max_length=1, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                  related_name='storage_create_by')
    enable = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.desc


class Location(models.Model):
    storage = models.ForeignKey(Storage, related_name='storage_location', on_delete=models.DO_NOTHING)
    location_code = models.CharField(max_length=10, primary_key=True)
    location_name = models.CharField(max_length=20, blank=False, null=False)
    desc = models.CharField(max_length=200, blank=True, null=True)
    mach_location_code = models.CharField(max_length=2, blank=True, null=True)
    type = models.ForeignKey(Storage_Type, related_name='location_type', on_delete=models.DO_NOTHING)
    enable = models.CharField(max_length=1, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                  related_name='location_create_by')

    def __str__(self):
        return self.desc


class Bin(models.Model):
    location = models.ForeignKey(Location, related_name='location_bin', on_delete=models.DO_NOTHING)
    bin_code = models.CharField(max_length=20, primary_key=True)
    bin_name = models.CharField(max_length=200, blank=True, null=True)
    enable = models.CharField(max_length=1, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                  related_name='bin_create_by')

    def __str__(self):
        return self.desc
