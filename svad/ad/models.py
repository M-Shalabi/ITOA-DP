from django.db import models

# Create your models here.
from django.db import models

    #data def
    #data manuplation
class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=20)
    

class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    is_civilian = models.BooleanField()
    is_military= models.BooleanField()
    is_international= models.BooleanField()

# Primary keys and Foreign keys and relationships 
# #one to many and one to one
#
#

class Aircraft_Type(models.Model):
    type = models.CharField(max_length=30)
    max_fuel_capacity = models.IntegerField()
    seats = models.IntegerField(max_length=6)

class Aircraft(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    production_year = models.DateField()
    status = models.CharField(max_length=30)
    fuel_level = models.FloatField()
    fuel_currency = models.CharField(max_length=3)


class AirportAircraftTypeAuth(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
