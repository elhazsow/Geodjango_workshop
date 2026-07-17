from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from sig_app.models import Region, Departement, Commune

region_mapping = {
    "name": "REG",
    "code": "CODE",
    "geom": "MULTIPOLYGON",  
}
dpt_mapping = {
    "region": {
        "name":"REG_2",
        },
    "name": "DEPT",
    "geom": "MULTIPOLYGON",  
}
commune_mapping = {
    "departement": {
        "name":"DEPT"
        },
    "name":"NOM_COMM",
    "geom": "MULTIPOLYGON",  
}


region_shp = Path(__file__).resolve().parent.joinpath("data","Limites_régions.shp")
dpt_shp = Path(__file__).resolve().parent.joinpath("data", "Limites_departements.shp")    
commune_shp = Path(__file__).resolve().parent.joinpath("data", "Limites_communes.shp")
def run(verbose=True):
    print('chargement régions ... ')
    lm_region = LayerMapping(Region, region_shp, region_mapping, transform=True)
    lm_region.save(strict=True, verbose=verbose)
    print('chargement régions effectif\n**********************************************\n  ')
    print('chargement départements ... ')
    lm_dpt = LayerMapping(Departement, dpt_shp, dpt_mapping, transform=True)
    lm_dpt.save(strict=True, verbose=verbose)
    print('chargement départements effectif \n**********************************************\n  ')
    print('chargement communes ... ')
    lm_commune = LayerMapping(Commune, commune_shp, commune_mapping, transform=True)
    lm_commune.save(strict=False, verbose=verbose)
    print('chargement communes effectif \n**********************************************\n  ')