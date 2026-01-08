from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

from .. permissions import checkUniEsse3ApiGroupPermission
from .. uniEsse3Api import uniEsse3ApiClient, UniEsse3APIView

from . settings import *


class CarriereAPIView(UniEsse3APIView):
    
    name = "Carriere Service V1"
    description = "https://unical.esse3.cineca.it/e3rest/docs/?urls.primaryName=Carriere%20Api%20V1%20(https%3A%2F%2Funical.esse3.cineca.it%2Fe3rest%2Fapi%2Fcarriere-service-v1)"
    permission_classes = [checkUniEsse3ApiGroupPermission(SERVICE)]
    
    def getCarriere(self, request):
        cf = request.GET.get('cf')
        if not cf:
            return Response(
                status=400,
                data="Parametro GET 'cf' (codice fiscale) mancante"
            )
        url = f'{self.client.base_url}/{SERVICE}/{CARRIERE}' + '?codFis={}'
        response = self.client.get(url.format(cf.upper()))
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=response.status_code)
