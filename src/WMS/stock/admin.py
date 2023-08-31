from django.contrib import admin
from stock.models import Storage_Type, Storage, Location, Bin


@admin.register(Storage_Type)
class Storage_TypeAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_name')


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('storage_code', 'type', 'desc', 'ip_addr', 'lift', 'access_point', 'enable')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('storage', 'location_code', 'location_name', 'desc', 'enable')


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'bin_code', 'bin_name', 'enable')
