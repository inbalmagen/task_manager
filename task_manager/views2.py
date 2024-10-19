from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'token/',
        'token/refresh/',
    ]

    return Response(routes)