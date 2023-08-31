from django.urls import re_path as url
from stock.views import excel_import, search, location_list, call_location

urlpatterns = [
    url(r'^import/', excel_import, name='stock_import'),
    url(r'^search/', search, name='stock_search'),
    url(r'^location/', location_list, name='location_list'),
    url(r'^call_location/', call_location, name='call_location'),
]
