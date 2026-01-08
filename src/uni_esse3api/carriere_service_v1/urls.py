from django.urls import path

from . settings import SERVICE
from . views import *


app_name = SERVICE


urlpatterns = [
    path('carriere/', CarriereAPIView.as_view()),
]
