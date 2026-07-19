from django.shortcuts import render
from django.core.serializers import serialize
from .models import Region
from django.contrib.gis.db.models.functions import Envelope


# Create your views here.

def map_view(request):
    regions = Region.objects.all()
    regions_json = serialize('geojson', regions, geometry_field='geom', fields=('name', 'code'))
    # print(communes_json)
    context = {'regions_json': regions_json}
    return render(request, 'map.html', context)
