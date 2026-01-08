from django.conf import settings

from drf_spectacular.utils import extend_schema

from rest_framework.decorators import action
from rest_framework.response import Response

from .. permissions import checkUniEsse3ApiGroupPermission
from .. uniEsse3Api import UniEsse3APIViewSet
from . settings import *
