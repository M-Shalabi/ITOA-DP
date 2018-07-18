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
    paginated = Flase

    def __init__(self, new_dict=None, **kwargs):
        if new_dict is not None:
            super().__init__(new_dict)
        else:
            super().__init__(**kwargs)
            
            
