from django.shortcuts import render
from django.views import View
from .models import Country,Aircraft,Aircraft_Type,Airport,City
from .forms import CountryForm

class Home(View):
    def get(self,request):
        return render(request,'ad/home_page.html')

class CountryManage(View):
    def get(self,request):
        return render(request,'ad/manage_country.html')

class CountryList(View):
    pass

    def get(self,request):
        status_code, is_serialized, countries = Country.get_list()
        country_form = CountryForm()
        context = {
            'countries':countries,
            'country_form':country_form,
        }
        return render(request,'ad/country_index.html',context)

    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetail(View):
    pass


class CityManage(View):
    def get(self,request):
        return render(request,'ad/manage_city.html')

class CityList(View):
    def get(self,request):
        status_code, is_serialized, cities = City.get_list()
        context = {
            'cities':cities
        }
        return render(request,'ad/city_index.html',context)

class CityDetail(View):
    pass     

class AirportList(View):

    def get(self,request):
        status_code, is_serialized, airports = Airport.get_list()
        context = {
            'airports':airports
        }
        return render(request,'ad/airport_index.html',context)

class AirportDetail(View):
    pass      

class Aircraft_TypeList(View):
    def get(self,request):
        status_code, is_serialized, aircraft_types = Aircraft_Type.get_list()
        context = {
            'aircraft_types':aircraft_types
        }
        return render(request,'ad/aircraft_types_index.html',context)

class Aircraft_TypeDetail(View):
    pass

class AircraftList(View):
    
    def get(self,request):
        status_code, is_serialized, aircrafts = Aircraft.get_list()
        context = {
            'aircrafts':aircrafts
        }
        return render(request,'ad/aircraft_index.html',context)
    
class AircraftDetail(View):
    pass