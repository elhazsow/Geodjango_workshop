from django.contrib import admin
from .models import Region, Departement, Commune, Point,Raster
from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis.admin import GISModelAdmin
from django.contrib.gis.forms.widgets import OpenLayersWidget, OSMWidget

# Register your models here.

@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    list_display=("name","code")

@admin.register(Departement)
class DepartementAdmin(GISModelAdmin):
    list_display=("name","region")
    
@admin.register(Commune)
class CommuneAdmin(LeafletGeoAdmin):
    list_display=("name","departement")


@admin.register(Point) 
class PointAdmin(LeafletGeoAdmin):
    list_display=("name","description") 
    
    
@admin.register(Raster) 
class RasterAdmin(GISModelAdmin):
    list_display=("name", "rst")