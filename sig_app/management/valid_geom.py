from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
# import osmnx as os
from pathlib import Path

shapefile = Path(__file__).resolve().parent.joinpath("data", "Limites_communes.shp")
ds = DataSource(shapefile)
layer = ds[0]

for i, feat in enumerate(layer):
    try:
        geom = feat.geom
        if not GEOSGeometry(geom.wkt).valid:
            place_name = f"{feat['NOM_COMM']}, {feat['DEPT']}, Senegal"
            print(place_name)
            print(f"Feature {i} -> Pas de géométrie! Nom: {feat['NOM_COMM']}")
    except Exception as e:
        # Nom de la commune
        
        # # Télécharger le polygone depuis OSM
        # gdf = ox.geocode_to_gdf(place_name)
        # # Prendre le polygone (OSMNX retourne un GeoDataFrame)
        # polygon = gdf.geometry.iloc[0]

        # # Convertir en WKT pour Django
        # wkt_geom = polygon.wkt
        # django_geom = GEOSGeometry(wkt_geom)
        # print(django_geom)
        print(f"Feature {i} -> Erreur: {e}")
