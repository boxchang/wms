from django.urls import re_path as url
from stock.views import excel_import, search, location_list, call_location, bin_list, item_import, wo_import, wo_search, \
    call_wo_item_check

urlpatterns = [
    url(r'^wo_search/', wo_search, name='wo_search'),
    url(r'^wo_import/', wo_import, name='wo_import'),
    url(r'^item_import/', item_import, name='item_import'),
    url(r'^import/', excel_import, name='stock_import'),
    url(r'^search/', search, name='stock_search'),
    url(r'^location/', location_list, name='location_list'),
    url(r'^bin/(?P<storage>\w+)/(?P<location>\w+)', bin_list, name='bin_list'),
    url(r'^call_location/', call_location, name='call_location'),
    url(r'^call_wo_item_check/', call_wo_item_check, name='call_wo_item_check'),
]
