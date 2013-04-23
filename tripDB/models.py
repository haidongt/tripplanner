from django.db import models

# Create your models here.

class Destination(models.Model):
    #dest_ID = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
    
class Route(models.Model):
    destA = models.CharField(max_length=200)
    destB = models.CharField(max_length=200)

class Attraction(models.Model):
    route = models.ForeignKey(Route)
    name = models.CharField(max_length=200)

