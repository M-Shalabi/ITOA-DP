import requests
from rest_framework import status as http_statuses
from common.models import BackendRequest, FrontendModel

# Create your models here.
class Country(FrontendModel):

    serializer_module = 'ad.serializers'
    serializer_class = 'CountrySerializer'
    view_serializer_class = 'CountrySerializer'
    index_url = 'ad/countries'
    detail_url = 'ad/countries/{0}'
    paginated = False

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            # for an example of city is an instance in Country, if its an integer store it as an int, if it's an object
            # store that object in a city instance inside the country .. example :-
            # if isinstance(kwargs['city'],int):
            #    self.city = kwargs['city']
            #    else:
            #        self.city = City(**kwargs['city'])

class City(FrontendModel):

    serializer_module = 'ad.serializers'
    serializer_class = 'CitySerializers'
    view_serializer_class = 'CitySerializers'
    index_url = 'ad/cities'
    detail_url = 'ad/cities/{0}'
    paginated = False

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            

class Airport(FrontendModel):

    serializer_module = 'ad.serializers'
    serializer_class = 'AirportSerializers'
    view_serializer_class = 'AirportSerializers'
    index_url = 'ad/airports'
    detail_url = 'ad/airports/{0}'
    paginated = False

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            
                        
class Aircraft(FrontendModel):

    serializer_module = 'ad.serializers'
    serializer_class = 'AircraftSerializers'
    view_serializer_class = 'AircraftSerializers'
    index_url = 'ad/aircrafts'
    detail_url = 'ad/aircrafts/{0}'
    paginated = False

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            

class Aircraft_Type(FrontendModel):

    serializer_module = 'ad.serializers'
    serializer_class = 'Aircraft_TypeSerializers'
    view_serializer_class = 'Aircraft_TypeSerializers'
    index_url = 'ad/aircraft_types'
    detail_url = 'ad/aircraft_types/{0}'
    paginated = False

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            
            


