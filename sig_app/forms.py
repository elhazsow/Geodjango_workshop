# from django.contrib.gis import forms 
from django import forms
from .models import Point
from leaflet.forms.widgets import LeafletWidget

# https://docs.djangoproject.com/fr/6.0/ref/contrib/gis/forms-api/

class PointForm(forms.ModelForm):
    
    class Meta:
        model = Point
        fields = ["name","description","location"]
        widgets={
            "location":LeafletWidget(),
            "name": forms.TextInput(attrs={'class':"form-control"}),
            "description":forms.Textarea(attrs={'class':'form-control'})
        }
 

# formulaire qui ne dépend pas d'un modèle

# class FormGeo(forms.Form):
    
#     name=forms.CharField()
#     description=forms.CharField(widget=forms.TextArea)
#     localisation=forms.PointField(widget=LeafletWidget(
#         attrs={
#            'display_raw':'true', 
#         }
#     ))
