from .models import Country, City, Airport, Aircraft_Type, Aircraft
from .serializers import CountrySerializers, CitySerializers, AirportSerializers, Aircraft_TypeSerializers, AircraftSerializers
# We removed AuthorizedTypesSerializers from .serializers import 
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Create your views here.
# We removed AuthorizedTypes class, so we removed it from .models import

# Views.py is the Controller in the MVC

class CountryList(APIView):
    #Check Django documentations
    # post for create
    # patch for update
    # get for read
    # delete for delete

    #put for complete update

 
    # HTTP METHODS  get , post
    # get list of countries
    def get(self,request):
        countries = Country.objects.all()
        serializer= CountrySerializers(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new country
    def post(self,request):
        serializer = CountrySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class CountryDetail(APIView):
    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializers(country)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializers(country,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CityList(APIView):

    # get list of cities
    def get(self,request):
        cities = City.objects.all()
        serializer= CitySerializers(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = CitySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class CityDetail(APIView):
    def get(self, request, pk):
        cities = get_object_or_404(City, pk=pk)
        serializer = CitySerializers(cities)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        cities = get_object_or_404(City, pk=pk)
        serializer = CitySerializers(cities,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        cities = get_object_or_404(City, pk=pk)
        cities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class AirportList(APIView):

    # get list of Airport
    def get(self,request):
        airports = Airport.objects.all()
        serializer= AirportSerializers(airports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new Airport
    def post(self,request):
        serializer = AirportSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class AirportDetail(APIView):

    def get(self, request, pk):
        airports = get_object_or_404(Airport, pk=pk)
        serializer = AirportSerializers(airports)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        airports = get_object_or_404(Airport, pk=pk)
        serializer = AirportSerializers(airports,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        airports = get_object_or_404(Airport, pk=pk)
        airports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class Aircraft_TypeList(APIView):

    # get list of Airport
    def get(self,request):
        aircraft_types = Aircraft_Type.objects.all()
        serializer= Aircraft_TypeSerializers(aircraft_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new Airport
    def post(self,request):
        serializer = Aircraft_TypeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class Aircraft_TypeDetail(APIView):

    def get(self, request, pk):
        aircraft_types = get_object_or_404(Aircraft_Type, pk=pk)
        serializer = Aircraft_TypeSerializers(aircraft_types)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        aircraft_types = get_object_or_404(Aircraft_Type, pk=pk)
        serializer = Aircraft_TypeSerializers(aircraft_types,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        aircraft_types = get_object_or_404(Aircraft_Type, pk=pk)
        aircraft_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

class AircraftList(APIView):

    # get list of cities
    def get(self,request):
        aircrafts = Aircraft.objects.all()
        serializer= AircraftSerializers(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = AircraftSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class AircraftDetail(APIView):
    def get(self, request, pk):
        aircrafts = get_object_or_404(Aircraft, pk=pk)
        serializer = AircraftSerializers(aircrafts)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        aircrafts = get_object_or_404(Aircraft, pk=pk)
        serializer = AircraftSerializers(aircrafts,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        aircrafts = get_object_or_404(Aircraft, pk=pk)
        aircrafts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
'''
    class AuthorizedTypesList(APIView):

    # get list of cities
    def get(self,request):
        authorized_types = AuthorizedTypes.objects.all()
        serializer= AuthorizedTypesSerializers(authorized_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = AuthorizedTypesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    class AuthorizedTypesDetail(APIView):
    def get(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        serializer = AuthorizedTypesSerializers(authorized_types)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        serializer = AuthorizedTypesSerializers(authorized_types,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        authorized_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
'''