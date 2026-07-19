from sig_app.models import Region, Departement, Commune
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry, Point, MultiPolygon



def run(verbose=True):
    # Charger les données des régions
    region_ds = DataSource('sig_app/scripts/data/Limites_régions.shp')
    region_layer = region_ds[0]
    print('couche regions:', region_layer.fields, region_layer.srs, region_layer.geom_type, region_layer.num_feat)
    # Charger les données des départements
    departement_ds = DataSource('sig_app/scripts/data/Limites_departements.shp')
    departement_layer = departement_ds[0]
    print('couche départements:', departement_layer.fields, departement_layer.srs, departement_layer.geom_type, departement_layer.num_feat)
 
    # Charger les données des communes
    commune_ds = DataSource('sig_app/scripts/data/Limites_communes.shp')
    commune_layer = commune_ds[0]
    print('couche communes:', commune_layer.fields, commune_layer.srs, commune_layer.geom_type, commune_layer.num_feat)
    