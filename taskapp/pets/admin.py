from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'address', 'city', 'pet_image')
