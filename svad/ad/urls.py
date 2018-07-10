from django.conf.urls import url
from . import views
app_name = 'ad'
urlpatterns = [
    url(r'countries$',views.CountryList.as_view(), name ='country_list'),
    url(r'countries/(?P<pk>[0-9]+)$',views.CountryDetail.as_view(), name = 'country_details'),

    url(r'countries/cities$',views.CityList.as_view(), name ='city_list'),
    url(r'countries/cities/(?P<pk>[0-9]+)$',views.CityDetail.as_view(), name = 'city_details'),

    url(r'countries/cities/airports$',views.AirportList.as_view(), name ='airport_list'),
    url(r'countries/cities/airports/(?P<pk>[0-9]+)$',views.AirportDetail.as_view(), name = 'airport_details'),
]