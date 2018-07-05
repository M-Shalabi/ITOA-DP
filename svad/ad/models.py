from django.db import models

# Create your models here.

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
    remarks = models.CharField(max_length=500)
    fuel_cost = models.IntegerField()
    fuel_currency = models.IntegerField()
    
# Primary keys and Foreign keys and relationships 
# #one to many and one to one
#
#

class Aircraft_Type(models.Model):
    aircraft_Type = models.CharField(max_length=25)
    max_fuel_capacity = models.IntegerField()
    first_class_seats=models.IntegerField(max_length=3)
    business_class_seats=models.IntegerField(max_length=3)
    economy_class_seats=models.IntegerField(max_length=3)

class Aircraft(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    production_year = models.DateField()
    status = models.CharField(max_length=30)
    fuel_level = models.FloatField()
    fuel_currency = models.CharField(max_length=3)


class AirportAircraftTypeAuth(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
