from django.conf.urls import url
from . import views
app_name = 'ad'
urlpatterns = [
    url(r'countries$',views.CountryList.as_view(), name ='country_list'),
    url(r'countries/(?P<pk>[0-9]+)$',views.CountryDetail.as_view(), name = 'country_details'),
]