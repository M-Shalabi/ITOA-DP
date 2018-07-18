from django.db import models

# Create your models here.
# It is the Models in MVC
# Models.py is for data defention & data manuplation
class Country(models.Model):
    name = models.CharField(max_length=30)

# create and update functions are optional , 
# we don't need them as there are already built in create and update !
# we define functions or override them when we need a special case

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    is_civilian = models.BooleanField()
    is_military= models.BooleanField()
    is_international= models.BooleanField()
    remarks = models.CharField(max_length=500)
    fuel_cost = models.FloatField()
    fuel_currency = models.CharField(max_length=500)


class Aircraft_Type(models.Model):
    authorized_airports = models.ManyToManyField(Airport , related_name='authorized_aircraft_types')
    aircraft_Type = models.CharField(max_length=25)
    max_fuel_capacity = models.IntegerField()
    first_class_seats=models.IntegerField()
    business_class_seats=models.IntegerField()
    economy_class_seats=models.IntegerField()
    
    # (Airport , through = 'AuthorizedTypes' , related_name='authorized_aircraft_types')
    # since we've not used class AuthorizedTypes we wont write through = 'AuthorizedTypes' 

class Aircraft(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    production_year = models.DateField()
    status = models.CharField(max_length=30)
    fuel_level = models.FloatField()
   
# We don't need this class, Django will create it since we made the Many to Many relation in Aircraft types
# and since we don't have any fields it's just the relations, from the airport and aircraft_type

#class AuthorizedTypes
'''
    class AuthorizedTypes(models.Model):
        airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
        aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
'''

'''
    @staticmethod
    def create(**kwargs):
        auth_types = AuthorizedTypes()
        auth_types.airport = kwargs.get('airport')
        auth_types.aircraft_type = kwargs.get('aircraft_type')
        auth_types.save()
        return auth_types

    def update(self, **kwargs):
        self.airport = kwargs.get('airport')
        self.aircraft_type = kwargs.get('aircraft_type')
        self.save()
        return self
'''
        