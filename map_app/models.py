from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class MarkedPlaces(models.Model):
    name = models.CharField(max_length=128)
    location = models.PointField(srid=4326)
    objects = GeoManager()
    
    def __str__(self):
        return self.name
    
    
