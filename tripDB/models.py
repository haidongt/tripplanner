from django.db import models

# Create your models here.

class Destination(models.Model):
    dest_ID = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class Route(models.Model):
    route_ID = models.IntegerField(default=0)
    dest_A_ID = models.IntegerField(default=0)
    dest_B_ID = models.IntegerField(default=0)
    driving_time = models.IntegerField(default=0)
    
