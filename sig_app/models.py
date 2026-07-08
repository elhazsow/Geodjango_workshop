from django.contrib.gis.db import models

# Create your models here.

class Point(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name
