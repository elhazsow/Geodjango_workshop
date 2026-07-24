from django.urls import path
from . import views


urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('create_point',views.formulaire,name="create_point")
    
]