from django.conf import settings

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from rest_framework.decorators import action
from rest_framework.response import Response

from .. permissions import checkUniEsse3ApiGroupPermission
from .. uniEsse3Api import UniEsse3APIViewSet
from . serializers import *
from . settings import *


@extend_schema(
    tags=['Esse3 - Carriere v1'],
    responses={200: OpenApiTypes.OBJECT},
    summary = "Carriere Service V1",
    description = "Basato sul servizio https://unical.esse3.cineca.it/e3rest/docs/?urls.primaryName=Carriere%20Api%20V1%20(https%3A%2F%2Funical.esse3.cineca.it%2Fe3rest%2Fapi%2Fcarriere-service-v1)"
)
class CarriereAPIViewSet(UniEsse3APIViewSet):
    permission_classes = [checkUniEsse3ApiGroupPermission(SERVICE)]

    @extend_schema(
        parameters=[CarriereRequestSerializer],
    )
    @action(detail=False, methods=['get'], url_path='carriere')
    def getCarriere(self, request):
        serializer = CarriereRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        cf = serializer.validated_data['cf']
        url = f'{self.client.base_url}/{SERVICE}/{CARRIERE}?codFis={cf.upper()}'
        response = self.client.get(url)
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=response.status_code)
