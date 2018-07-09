from .models import Country
from .serializers import CountrySerializers
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
        pass