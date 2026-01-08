from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .. routers import NoSlashRouter
from . views import CarriereAPIViewSet


router = NoSlashRouter()
router.register('', CarriereAPIViewSet, basename='carriere')

urlpatterns = [
    path('', include(router.urls)),
]
