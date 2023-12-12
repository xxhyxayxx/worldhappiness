# api/views.py

from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.serializers import WorldHappinessTokenObtainPairSerializer, RegisterSerializer, CountrySerializer, RegionSerializer, CountryRegionSerializer, EconomicDataSerializer, YearSerializer
from .models import Country, Region, CountryRegion, EconomicData, Year

class WorldHappinessTokenObtainPairView(TokenObtainPairView):
    serializer_class = WorldHappinessTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/test/'
    ]
    return Response(routes)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]

class CountryRegionViewSet(viewsets.ModelViewSet):
    queryset = CountryRegion.objects.all()
    serializer_class = CountryRegionSerializer
    permission_classes = [IsAuthenticated]

class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [IsAuthenticated]

class EconomicDataViewSet(viewsets.ModelViewSet):
    queryset = EconomicData.objects.all()
    serializer_class = EconomicDataSerializer
    permission_classes = [IsAuthenticated]
