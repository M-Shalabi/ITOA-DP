from django.conf.urls import url
from . import views
app_name = 'ad'
urlpatterns = [
    url(r'countries$',views.CountryList.as_view(), name ='country_list'),
    url(r'countries/(?P<pk>[0-9]+)$',views.CountryDetail.as_view(), name = 'country_details'),

    # if you want a city for a specific country
    # it should be like this " countries/(?P<pk>[0-9]+)/cities "

    url(r'cities$',views.CityList.as_view(), name ='city_list'),
    url(r'cities/(?P<pk>[0-9]+)$',views.CityDetail.as_view(), name = 'city_details'),

    url(r'airports$',views.AirportList.as_view(), name ='airport_list'),
    url(r'airports/(?P<pk>[0-9]+)$',views.AirportDetail.as_view(), name = 'airport_details'),


    url(r'aircraft_types$',views.Aircraft_TypeList.as_view(), name ='aircraft_types_list'),
    url(r'aircraft_types/(?P<pk>[0-9]+)$',views.Aircraft_TypeDetail.as_view(), name = 'aircraft_types_details'),


    url(r'aircrafts$',views.AircraftList.as_view(), name ='aircrafts_list'),
    url(r'aircrafts/(?P<pk>[0-9]+)$',views.AircraftDetail.as_view(), name = 'aircrafts_details'),


    #We don't need this anymore since we now have authorized_airports
    #many to many relationship in Aircraft_Type class
    #url(r'countries/cities/airports/aircraft_types/aircrafts/authorized_types$',views.AuthorizedTypesList.as_view(), name ='authorized_types_list'),
    #url(r'countries/cities/airports/aircraft_types/aircrafts/authorized_types/(?P<pk>[0-9]+)$',views.AuthorizedTypesDetail.as_view(), name = 'authorized_types_details'),

]