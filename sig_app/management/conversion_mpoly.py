from osgeo import ogr
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
from pathlib import Path

# Ouvrir le shapefile
shapefile=Path(__file__).resolve().parent.joinpath("data", "Limites_communes.shp")
ds = ogr.Open(shapefile)
layer = ds.GetLayer(0)

for feature in layer:
    ogr_geom = feature.GetGeometryRef()
    if ogr_geom is None:
        print("Géométrie invalide pour feature id", feature.GetFID())
        continue

    wkt = ogr_geom.ExportToWkt()
    geom = GEOSGeometry(wkt)

    # Conversion systématique en MultiPolygon
    if geom.geom_type == 'Polygon':
        geom = MultiPolygon(geom)

    print(f"Feature {feature.GetFID()} -> {geom.geom_type}")
