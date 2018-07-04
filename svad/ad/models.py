from django.db import models

# Create your models here.
from django.db import models

    #data def
    #data manuplation
class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

# Primary keys and Foreign keys and relationships 
# #one to many and one to one
#
#

class Aircraft(models.Model):
    pass

class AirportAircraftTypeAuth(models.Model):
    pass

