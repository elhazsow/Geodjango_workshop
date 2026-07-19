from sig_app.models import Region, Departement, Commune
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry, Point, MultiPolygon
from django.db.models import F



def run(verbose=True):
    #requête pour récupérer toutes les régions
    regions = Region.objects.all()[0:5]  # Exemple : récupérer les 5 premières régions
    for region in regions:
        print(f" - {region.name}")
        
    #requête pour récupérer tous les départements d'une région spécifique (par exemple, la première région)
    first_departement = Departement.objects.filter(name="TIVAOUANE").first()
    if first_departement:
        region = Region.objects.filter(geom__contains=first_departement.geom)
        for region in region:
            print(f"Département {first_departement.name} appartient à la région {region.name}")
            print(f" - {round(region.geom.area/10000, 2)} ha")
        
        