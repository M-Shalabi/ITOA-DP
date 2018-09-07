from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'ad'
urlpatterns = [

    url(r'home$',views.Home.as_view(), name ='home_page'),

    url(r'countries$',views.CountryList.as_view(), name ='country_list'),
    url(r'countries/manage$',views.CountryManage.as_view(), name ='country_manage'),
    url(r'countries/(?P<pk>[0-9]+)$',views.CountryDetail.as_view(), name = 'country_details'),

    # if you want a city for a specific country
    # it should be like this " countries/(?P<pk>[0-9]+)/cities "

    url(r'cities$',views.CityList.as_view(), name ='city_list'),
    url(r'cities/manage$',views.CityManage.as_view(), name ='city_manage'),
    url(r'cities/(?P<pk>[0-9]+)$',views.CityDetail.as_view(), name = 'city_details'),

    url(r'airports$',views.AirportList.as_view(), name ='airport_list'),
    url(r'airports/(?P<pk>[0-9]+)$',views.AirportDetail.as_view(), name = 'airport_details'),


    url(r'aircraft_types$',views.Aircraft_TypeList.as_view(), name ='aircraft_types_list'),
    url(r'aircraft_types/(?P<pk>[0-9]+)$',views.Aircraft_TypeDetail.as_view(), name = 'aircraft_types_details'),


    url(r'aircrafts$',views.AircraftList.as_view(), name ='aircrafts_list'),
    url(r'aircrafts/(?P<pk>[0-9]+)$',views.AircraftDetail.as_view(), name = 'aircrafts_details'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)