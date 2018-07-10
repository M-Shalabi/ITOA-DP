from .models import Country, City, Airport
from .serializers import CountrySerializers, CitySerializers, AirportSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Create your views here.


class CountryList(APIView):
 #Check Django documentations
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
        airport = Airport.objects.all()
        serializer= AirportSerializers(airport, many=True)
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
        airport = get_object_or_404(City, pk=pk)
        serializer = AirportSerializers(airport)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def patch(self, request, pk):
        airport = get_object_or_404(City, pk=pk)
        serializer = AirportSerializers(airport,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors , status = status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        airport = get_object_or_404(City, pk=pk)
        airport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
