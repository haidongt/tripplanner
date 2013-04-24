from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Destination(models.Model):
    #dest_ID = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    
class Route(models.Model):
    destA = models.CharField(max_length=200)
    destB = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Attraction(models.Model):
    route = models.ForeignKey(Route)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

