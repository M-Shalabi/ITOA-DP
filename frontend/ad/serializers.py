from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class City(serializers.Serializer):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Airport(serializers.Serializer):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    is_civilian = models.BooleanField()
    is_military= models.BooleanField()
    is_international= models.BooleanField()
    remarks = models.CharField(max_length=500)
    fuel_cost = models.FloatField()
    fuel_currency = models.CharField(max_length=500)

class Aircraft_Type(serializers.Serializer):
    authorized_airports = models.ManyToManyField(Airport , related_name='authorized_aircraft_types')
    aircraft_Type = models.CharField(max_length=25)
    max_fuel_capacity = models.IntegerField()
    first_class_seats=models.IntegerField()
    business_class_seats=models.IntegerField()
    economy_class_seats=models.IntegerField()


class Aircraft(serializers.Serializer):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    aircraft_type = models.ForeignKey(Aircraft_Type,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    production_year = models.DateField()
    status = models.CharField(max_length=30)
    fuel_level = models.FloatField()    