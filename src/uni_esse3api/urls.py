from django.urls import include, path

from . anagrafica_service_v2 import urls as anagrafica_service_v2_urls
from . anagrafica_service_v2.settings import SERVICE as anagrafica_v2_service_prefix
from . carriere_service_v1 import urls as carriere_service_v1_urls
from . carriere_service_v1.settings import SERVICE as carriere_service_v1_prefix
from . utenti_service_v1 import urls as utenti_service_v1_urls
from . utenti_service_v1.settings import SERVICE as utenti_service_v1_prefix

from . settings import ESSE3_PREFIX


app_name = 'uni_esse3api'

urlpatterns = []
urlpatterns += [
    path(f'{ESSE3_PREFIX}/{anagrafica_v2_service_prefix}/', include(anagrafica_service_v2_urls)),
    path(f'{ESSE3_PREFIX}/{carriere_service_v1_prefix}/', include(carriere_service_v1_urls)),
    path(f'{ESSE3_PREFIX}/{utenti_service_v1_prefix}/', include(utenti_service_v1_urls)),
]
