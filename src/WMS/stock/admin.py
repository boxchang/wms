from django.contrib import admin
from stock.models import Storage_Type, Storage, Location, Bin, Access_Point


@admin.register(Access_Point)
class Access_PointAdmin(admin.ModelAdmin):
    list_display = ('point_code', 'point_name', 'desc')


@admin.register(Storage_Type)
class Storage_TypeAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_name')


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('storage_code', 'type', 'desc', 'ip_addr', 'lift', 'enable')
    filter_horizontal = ('access_point',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('storage', 'location_code', 'location_name', 'desc', 'enable')


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('location', 'bin_code', 'bin_name', 'enable')
