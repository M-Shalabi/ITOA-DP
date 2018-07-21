from .models import Country, City, Airport, Aircraft_Type, Aircraft
from .serializers import CountrySerializer, CitySerializer, AirportSerializer, Aircraft_TypeSerializer, AircraftSerializer
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
        serializer= CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new country
    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetail(APIView):
    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(country,data=request.data, partial=True)
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
        country_pk = request.query_params.get('country', None)
        cities = City.objects.all()
        if country_pk:
            cities = cities.filter(country__id=country_pk)
        serializer= CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(APIView):

    def get(self, request, pk):
        cities = get_object_or_404(City, pk=pk)
        serializer = CitySerializer(cities)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        cities = get_object_or_404(City, pk=pk)
        serializer = CitySerializer(cities,data=request.data, partial=True)
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
        city_pk = request.query_params.get('city', None)
        airports = Airport.objects.all()
        if city_pk:
            airports = airports.filter(city__id=city_pk)
        serializer= AirportSerializer(airports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new Airport
    def post(self,request):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AirportDetail(APIView):

    def get(self, request, pk):
        airports = get_object_or_404(Airport, pk=pk)
        serializer = AirportSerializer(airports)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        airports = get_object_or_404(Airport, pk=pk)
        serializer = AirportSerializer(airports,data=request.data, partial=True)
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
        serializer= Aircraft_TypeViewSerializer(aircraft_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new Airport
    def post(self,request):
        serializer = Aircraft_TypeViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aircraft_TypeDetail(APIView):

    def get(self, request, pk):
        aircraft_types = get_object_or_404(Aircraft_Type, pk=pk)
        serializer = Aircraft_TypeSerializer(aircraft_types)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        aircraft_types = get_object_or_404(Aircraft_Type, pk=pk)
        serializer = Aircraft_TypeSerializer(aircraft_types,data=request.data, partial=True)
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
        airport_pk = request.query_params.get('airport', None)
        aircrafts = Aircraft.objects.all()
        if airport_pk:
            aircrafts = aircrafts.filter(airport=airport_pk)
        serializer= AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AircraftDetail(APIView):
    def get(self, request, pk):
        aircrafts = get_object_or_404(Aircraft, pk=pk)
        serializer = AircraftSerializer(aircrafts)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        aircrafts = get_object_or_404(Aircraft, pk=pk)
        serializer = AircraftSerializer(aircrafts,data=request.data, partial=True)
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
        serializer= AuthorizedTypesSerializer(authorized_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # create a new city
    def post(self,request):
        serializer = AuthorizedTypesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    class AuthorizedTypesDetail(APIView):
    def get(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        serializer = AuthorizedTypesSerializer(authorized_types)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        serializer = AuthorizedTypesSerializer(authorized_types,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        authorized_types = get_object_or_404(AuthorizedTypes, pk=pk)
        authorized_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
'''