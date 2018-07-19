from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)


class CitySerializer(serializers.Serializer):
    country = CountrySerializer()
    name = serializers.CharField(max_length=20)
    country = serializers.IntegerField()

class AirportSerializer(serializers.Serializer):
    city = CitySerializer()
    name = serializers.CharField(max_length=60)
    is_civilian = serializers.BooleanField()
    is_military= serializers.BooleanField()
    is_international= serializers.BooleanField()
    remarks = serializers.CharField(max_length=500)
    fuel_cost = serializers.FloatField()
    fuel_currency = serializers.CharField(max_length=500)

class Aircraft_TypeSerializer(serializers.Serializer):
    authorized_airports = AirportSerializer(many=True)
    aircraft_Type = serializers.CharField(max_length=25)
    max_fuel_capacity = serializers.IntegerField()
    first_class_seats=serializers.IntegerField()
    business_class_seats=serializers.IntegerField()
    economy_class_seats=serializers.IntegerField()


class AircraftSerializer(serializers.Serializer):
    airports = AirportSerializers()
    aircraft_type = Aircraft_TypeSerializer()
    name = serializers.CharField(max_length=30)
    location = serializers.CharField(max_length=40)
    production_year = serializers.DateField()
    status = serializers.CharField(max_length=30)
    fuel_level = serializers.FloatField()    

    # Remove the foriegn