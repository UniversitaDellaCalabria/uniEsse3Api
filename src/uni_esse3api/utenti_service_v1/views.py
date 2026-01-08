from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

from .. permissions import checkUniEsse3ApiGroupPermission
from .. uniEsse3Api import uniEsse3ApiClient, UniEsse3APIView

from . settings import *
