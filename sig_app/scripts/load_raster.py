from sig_app.models import Raster
from django.contrib.gis.gdal import GDALRaster

# https://docs.djangoproject.com/fr/6.0/ref/contrib/gis/gdal/

def run(verbose=True):
    print("Chargement Raster DTM")
    dtmDk=r"D:\téléchargement\DTM_dakar\sow\DKR.tif"
    rast=GDALRaster(dtmDk, write=True)
    raster=Raster(name="DTM Dakar", rst=rast)
    raster.save()
    print("Image raster chargée:", raster.name)