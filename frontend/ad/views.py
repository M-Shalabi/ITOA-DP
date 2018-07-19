from django.shortcuts import render
from django.views import View
from .models import Country

class CountryList(View):
    pass

    def get(self,request):
        status_code, is_serialized, countries = Country.get_list()
        context = {
            'countries':countries
        }
        #if status_code == 200 remove if not used idk why he talked about it
        return render(request,'ad/country_index.html',context)

    #COMPLETE FROM HERE
    def post():
        pass

class CountryDetail(View):
    pass

class CityList(View):
    pass

class CityDetail(View):
    pass     

class AirportList(View):
    pass

class AirportDetail(View):
    pass      

class Aircraft_TypeList(View):
    pass

class Aircraft_TypeDetail(View):
    pass

class AircraftList(View):
    pass
    
class AircraftDetail(View):
    pass