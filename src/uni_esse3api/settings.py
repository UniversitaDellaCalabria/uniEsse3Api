from django.conf import settings

ESSE3_PREFIX = 'esse3'

ESSE3_API_BASE_URL = getattr(settings, 'ESSE3_API_BASE_URL', 'https://unical.esse3.cineca.it/e3rest/api')
ESSE3_API_USERNAME = getattr(settings, 'ESSE3_API_USERNAME', '')
ESSE3_API_PASSWORD = getattr(settings, 'ESSE3_API_PASSWORD', '')
