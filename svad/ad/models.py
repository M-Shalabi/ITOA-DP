from django.db import models

# Create your models here.

    #data def
    #data manuplation
class Country(models.Model):
    name = models.CharField(max_length=30)

# create and update functions are optional , 
# we don't need them as there are already built in create and update !
# we define functions or override them when we need a special case

    @staticmethod
    def create(**kwargs):
        country = Country()
        country.name = kwargs.get('name')
        country.save()
        return country

    def update(self, **kwargs):
        self.name = kwargs.get('name')
        self.save()
        return self
    


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    @staticmethod
    def create(**kwargs):
        city = City()
        city.name = kwargs.get('name')
        city.country = kwargs.get('country')
        city.save()
        return city

    def update(self, **kwargs):
        self.name = kwargs.get('name')
        self.country = kwargs.get('country')
        self.save()
        return self


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    is_civilian = models.BooleanField()
    is_military= models.BooleanField()
    is_international= models.BooleanField()
    remarks = models.CharField(max_length=500)
    fuel_cost = models.IntegerField()
    fuel_currency = models.IntegerField()


    @staticmethod
    def create(**kwargs):
        airport = Airport()
        airport.city = kwargs.get('city')
        airport.name = kwargs.get('name')
        airport.is_civilian = kwargs.get('is_civilian')
        airport.is_military = kwargs.get('is_military')
        airport.is_international = kwargs.get('is_international')
        airport.remarks = kwargs.get('remarks')
        airport.fuel_cost =kwargs.get('fuel_cost')
        airport.fuel_currency = kwargs.get('fuel_currency')
        airport.save()
        return airport

    def update(self, **kwargs):
        self.city = kwargs.get('city')
        self.name = kwargs.get('name')
        self.is_civilian = kwargs.get('is_civilian')
        self.is_military = kwargs.get('is_military')
        self.is_international = kwargs.get('is_international')
        self.remarks = kwargs.get('remarks')
        self.fuel_cost =kwargs.get('fuel_cost')
        self.fuel_currency = kwargs.get('fuel_currency')
        self.save()
        return self
# Primary keys and Foreign keys and relationships
# #one to many and one to one
#
#

class Aircraft_Type(models.Model):
    aircraft_Type = models.CharField(max_length=25)
    max_fuel_capacity = models.IntegerField()
    first_class_seats=models.IntegerField()
    business_class_seats=models.IntegerField()
    economy_class_seats=models.IntegerField()

    @staticmethod
    def create(**kwargs):
        aircraft_type = Aircraft_Type()
        aircraft_type.aircraft_Type = kwargs.get('aircraft_Type')
        aircraft_type.max_fuel_capacity = kwargs.get('max_fuel_capacity')
        aircraft_type.first_class_seats = kwargs.get('first_class_seats')
        aircraft_type.business_class_seats = kwargs.get('business_class_seats')
        aircraft_type.economy_class_seats = kwargs.get('economy_class_seats')
        aircraft_type.save()
        return aircraft_type

    def update(self, **kwargs):
        self.aircraft_Type = kwargs.get('aircraft_Type')
        self.max_fuel_capacity = kwargs.get('max_fuel_capacity')
        self.first_class_seats = kwargs.get('first_class_seats')
        self.business_class_seats = kwargs.get('business_class_seats')
        self.economy_class_seats = kwargs.get('economy_class_seats')
        self.save()
        return self


class Aircraft(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    production_year = models.DateField()
    status = models.CharField(max_length=30)
    fuel_level = models.FloatField()
    

    @staticmethod
    def create(**kwargs):
        aircraft = Aircraft()
        aircraft.airport = kwargs.get('airport')
        aircraft.aircraft_Type = kwargs.get('aircraft_Type')
        aircraft.name = kwargs.get('name')
        aircraft.location = kwargs.get('location')
        aircraft.production_year =kwargs.get('production_year')
        aircraft.status = kwargs.get('status')
        aircraft.fuel_level = kwargs.get('fuel_level')
        aircraft.save()
        return aircraft

    def update(self, **kwargs):
        self.airport = kwargs.get('airport')
        self.aircraft_Type = kwargs.get('aircraft_Type')
        self.name = kwargs.get('name')
        self.location = kwargs.get('location')
        self.production_year =kwargs.get('production_year')
        self.status = kwargs.get('status')
        self.fuel_level = kwargs.get('fuel_level')
        self.save()
        return self


class AuthorizedTypes(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)

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