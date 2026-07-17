from django.contrib import admin
from .models import Region, Departement, Commune
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    list_display=("name","code")

@admin.register(Departement)
class DepartementAdmin(LeafletGeoAdmin):
    list_display=("name","region")
    
@admin.register(Commune)
class CommuneAdmin(LeafletGeoAdmin):
    list_display=("name","departement")