import json
import requests

from django.conf import settings

from rest_framework import viewsets
from rest_framework.views import APIView

from . settings import *
from . utils import e3_basic_token


class uniEsse3ApiClient(object):

    def __init__(self):
        _username = ESSE3_API_USERNAME
        _password = ESSE3_API_PASSWORD
        self.token = e3_basic_token(_username, _password)
        self.base_url = ESSE3_API_BASE_URL

    def get(self, url):
        headers = {'Authorization': 'Basic {}'.format(self.token)}
        response = requests.get(url, headers=headers)
        return response


class UniEsse3APIViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = uniEsse3ApiClient()
