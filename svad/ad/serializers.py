from rest_framework import serializers
from .models import Country,Aircraft,Aircraft_Type,Airport,City
# We removed AuthorizedTypes class, so we removed it from .modelsimport
#This is Serlizer Model way, we took the fields from the model, 
# otherwise we would've wrote all the fields again
# it is The view in the MVC 
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        read_only_fields=('id',)
        # do i have to remove the , ? or not

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
# We named this Aircraft_TypeViewSerializers , we will return here everything including the relationship 
# because it's nested jason data we need to return it
class Aircraft_TypeViewSerializers(serializers.ModelSerializer):
    airports = AirportSerializers(many=True)
    class Meta:
        model = Aircraft_Type
        fields = '__all__'
        read_only_fields=('id',)


# We removed this since we don't have class AuthriedTypes
#  we don't need it anymore because there are no fields
'''
    class AuthorizedTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedTypes
        fields = '__all__'
        read_only_fields = ('id',)
'''