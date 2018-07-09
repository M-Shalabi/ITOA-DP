from rest_framework import serializers
from .models import Country,Aircraft,Aircraft_Type,Airport,City,AuthorizedTypes

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields=('id',)

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        read_only_fields=('id',)

class AircraftSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'
        read_only_fields=('id',)

class Aircraft_TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aircraft_Type
        fields = '__all__'
        read_only_fields=('id',)

class AirportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
        read_only_fields=('id',)

class AuthorizedTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedTypes
        fields = '__all__'
        read_only_fields = ('id',)