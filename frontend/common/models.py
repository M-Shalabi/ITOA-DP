import requests
from django.conf import settings
from rest_framework import status as http_statuses

BASE_URL = settings.BACKEND_URL


class BackendRequest:

    def __init__(self, app_url):
        self.url = '{0}/{1}'.format(BASE_URL, app_url)

    def post(self, params=None):
        response = requests.post(self.url, data=params)
        return BackendRequest.parse_response(response)

    def get(self, params=None):
        response = requests.get(self.url, params=params)
        return BackendRequest.parse_response(response)

    def put(self, params=None):
        response = requests.put(self.url, data=params)
        return BackendRequest.parse_response(response)

    def patch(self, params=None):
        response = requests.patch(self.url, data=params)
        return BackendRequest.parse_response(response)

    def delete(self, params=None):
        response = requests.delete(self.url, params=params)
        return BackendRequest.parse_response(response)

    @staticmethod
    def parse_response(response):
        if response.status_code == http_statuses.HTTP_200_OK or response.status_code == http_statuses.HTTP_201_CREATED:
            if response.text:
                object_json = response.json()
                return response.status_code, object_json
            else:
                return response.status_code

        elif response.status_code == http_statuses.HTTP_204_NO_CONTENT:
            return response.status_code, None

        elif response.status_code == http_statuses.HTTP_400_BAD_REQUEST:
            errors = response.json()
            return response.status_code, errors

        elif response.status_code == http_statuses.HTTP_401_UNAUTHORIZED:
            errors = {'Authentication': 'Unauthorized'}
            return response.status_code, errors

        elif response.status_code == http_statuses.HTTP_403_FORBIDDEN:
            errors = {'Permission': 'Forbidden'}
            return response.status_code, errors

        elif response.status_code == http_statuses.HTTP_404_NOT_FOUND:
            errors = {'Error': 'Not Found'}
            return response.status_code, errors

        elif response.status_code == http_statuses.HTTP_500_INTERNAL_SERVER_ERROR:
            errors = {'Server': 'Internal Server Error'}
            return response.status_code, errors

        else:
            # log error
            return None, None


class FrontendModel(object):

    serializer_module = ''
    serializer_class = ''
    view_serializer_class = ''
    index_url = ''
    detail_url = ''
    paginated = False

    id = ''

    def __init__(self, new_dict=None, **kwargs):
        if self.serializer_class and not self.view_serializer_class:
            self.view_serializer_class = self.serializer_class

        if new_dict is not None:
            for k, v in new_dict.items():
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    @classmethod
    def import_class(cls, module_name, class_name):
        module_ = import_module(module_name)
        class_ = getattr(module_, class_name)
        return class_

    def as_dict(self):
        model_dict = {}
        for k, v in vars(self).items():
            model_dict[k] = v

        return model_dict

    def save(self, token, parent_pk=None):
        if parent_pk:
            url = self.index_url.format(parent_pk)
        else:
            url = self.index_url

        params = {}
        for k, v in vars(self).items():
            params[k] = v

        request = FoisRequest(url, token)
        print('params {0}'.format(params))
        request_status, data = request.post(params=params)
        if request_status == http_statuses.HTTP_201_CREATED:
            serializer_status, object_instance = self.deserialize(data)
            return request_status, serializer_status, object_instance
        else:
            return request_status, False, data

    def update(self, token):
        params = {}
        for k, v in vars(self).items():
            params[k] = v

        request = FoisRequest(self.detail_url.format(self.id), token)
        request_status, data = request.patch(params=params)
        if request_status == http_statuses.HTTP_200_OK:
            serializer_status, object_instance = self.deserialize(data)
            return request_status, serializer_status, object_instance
        else:
            return request_status, False, data

    def delete(self, token):
        url = self.detail_url.format(self.id)
        request = FoisRequest(url, token)
        request_status, data = request.delete()
        return request_status, False, data

    @classmethod
    def get_list(cls, token, parent_pk=None, cursor=None, query_params=None):
        if parent_pk:
            url = cls.index_url.format(parent_pk)
        else:
            url = cls.index_url

        params = {}
        if query_params:
            params = query_params
        if cursor:
            params['cursor'] = cursor

        request = FoisRequest(url, token)
        if params:
            request_status, data = request.get(params=params)
        else:
            request_status, data = request.get()
        print(data)
        if request_status == http_statuses.HTTP_200_OK:
            serializer_status, object_list = cls.deserialize(data, many=True, view=True)
            return request_status, serializer_status, object_list
        else:
            return request_status, False, data

    @classmethod
    def get(cls, object_id, token):
        url = cls.detail_url.format(object_id)
        request = FoisRequest(url, token)
        request_status, data = request.get()
        if request_status == http_statuses.HTTP_200_OK:
            serializer_status, object_instance = cls.deserialize(data, view=True)
            return request_status, serializer_status, object_instance
        else:
            return request_status, False, data

    @classmethod
    def deserialize(cls, json_data, many=False, view=False):
        if view:
            serializer_class = cls.import_class(cls.serializer_module, cls.view_serializer_class)
        else:
            serializer_class = cls.import_class(cls.serializer_module, cls.serializer_class)

        if many:
            if cls.paginated:
                data = json_data['results']
            else:
                data = json_data
            serializer = serializer_class(data=data, many=True)
            if serializer.is_valid():
                object_list = []
                validated_json = serializer.validated_data
                for object_json in validated_json:
                    object_instance = cls(**object_json)
                    object_list.append(object_instance)
                return True, object_list
            else:
                return False, serializer.errors
        else:
            serializer = serializer_class(data=json_data)
            if serializer.is_valid():
                object_instance = cls(**serializer.validated_data)
                return True, object_instance
            else:
                return False, serializer.errors