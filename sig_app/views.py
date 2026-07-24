from django.shortcuts import render
from django.core.serializers import serialize
from .models import Region, Commune
from django.contrib.gis.db.models.functions import Envelope
from .forms import PointForm
from django.http import HttpResponse



# Create your views here.

def map_view(request):
    regions = Region.objects.all()
    communes=Commune.objects.all()
    regions_json = serialize('geojson', regions, geometry_field='geom', fields=('name', 'code'))
    com_json=serialize('geojson',communes,geometry_field='geom', fields=('name'))
    # print(communes_json)
    context = {'regions_json': regions_json,
               'communes':com_json}
    return render(request, 'map.html', context)


def formulaire(request):
    if request.method=="POST":
        form=PointForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Vos données sont bien enregistrées dans la base de données")
    
    form = PointForm()

    context={
        "form":form
    }
    
    return render(request, "formulaire.html", context)
            
    
