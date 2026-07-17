from django.contrib.gis.db import models

# Create your models here.

# class Point(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     #champs geographique pour stocker les coordonnées géographiques (latitude et longitude)
#     location = models.PointField(srid=4326)

#     def __str__(self):
#         return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5, unique=True)
    geom = models.MultiPolygonField(srid=32628,null=True, blank=True)
    class Meta:
        ordering=['name']
    
    def __str__(self): return self.name

class Departement(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='départements')
    geom = models.MultiPolygonField(srid=32628,null=True, blank=True)
    name = models.CharField(max_length=100)
    class Meta:
        ordering=['name']
    def __str__(self): return self.name

class Commune(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name="communes")
    geom=models.MultiPolygonField(srid=32628,null=True, blank=True)
    name = models.CharField(max_length=100)
    class Meta:
        ordering=['name']
    def __str__(self): return self.name