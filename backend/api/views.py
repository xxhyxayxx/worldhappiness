# api/views.py

from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.serializers import WorldHappinessTokenObtainPairSerializer, RegisterSerializer, CountrySerializer, RegionSerializer, CountryRegionSerializer, EconomicDataSerializer, YearSerializer, SocialSupportDataSerializer, HealthDataSerializer, HappinessScoreSerializer, FreedomDataSerializer, GovernmentTrustDataSerializer, GenerosityDataSerializer
from .models import Country, Region, CountryRegion, EconomicData, Year, SocialSupportData, HealthData, HappinessScore, FreedomData, GovernmentTrustData, GenerosityData
from django.shortcuts import render

class WorldHappinessTokenObtainPairView(TokenObtainPairView):
    serializer_class = WorldHappinessTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().prefetch_related('regions')
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

class SocialSupportDataViewSet(viewsets.ModelViewSet):
    queryset = SocialSupportData.objects.all()
    serializer_class = SocialSupportDataSerializer
    permission_classes = [IsAuthenticated]

class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    permission_classes = [IsAuthenticated]
    
class FreedomDataViewSet(viewsets.ModelViewSet):
    queryset = FreedomData.objects.all()
    serializer_class = FreedomDataSerializer
    permission_classes = [IsAuthenticated]

class HappinessScoreViewSet(viewsets.ModelViewSet):
    queryset = HappinessScore.objects.all()
    serializer_class = HappinessScoreSerializer
    permission_classes = [IsAuthenticated]
    
class GovernmentTrustDataViewSet(viewsets.ModelViewSet):
    queryset = GovernmentTrustData.objects.all()
    serializer_class = GovernmentTrustDataSerializer
    permission_classes = [IsAuthenticated]
    
class GenerosityDataViewSet(viewsets.ModelViewSet):
    queryset = GenerosityData.objects.all()
    serializer_class = GenerosityDataSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def getRoutes(request):
    routes = {
        'API': ('http://127.0.0.1:8000/api/', 'Root URL for the API.'),
        'Admin': ('http://127.0.0.1:8000/admin/', 'Link to the Django admin page.'),
        'Token Obtain': ('http://127.0.0.1:8000/api/token/', 'Endpoint to obtain a new JWT token.'),
        'Token Refresh': ('http://127.0.0.1:8000/api/token/refresh/', 'Endpoint to refresh your JWT token.'),
        'Register': ('http://127.0.0.1:8000/api/register/', 'Endpoint to create a new user account.'),
        'Countries List': ('http://127.0.0.1:8000/api/countries/', 'GET: Endpoint to list countries, POST: Endpoint to create a country.'),
        'Regions List': ('http://127.0.0.1:8000/api/regions/', 'GET: Endpoint to list regions, POST: Endpoint to create a region.'),
        'Country Regions List': ('http://127.0.0.1:8000/api/countryregions/', 'GET: Endpoint to list country-region relationships, POST: Endpoint to create a country-region relationship.'),
        'Economic Data List': ('http://127.0.0.1:8000/api/economicdata/', 'GET: Endpoint to list economic data entries, POST: Endpoint to create an economic data entry.'),
        'Year Data List': ('http://127.0.0.1:8000/api/years/', 'GET: Endpoint to list years, POST: Endpoint to create a year entry.'),
        'Social Support Data List': ('http://127.0.0.1:8000/api/socialsupportdata/', 'GET: Endpoint to list social support data entries, POST: Endpoint to create a social support data entry.'),
        'Health Data List': ('http://127.0.0.1:8000/api/healthdata/', 'GET: Endpoint to list health data entries, POST: Endpoint to create a health data entry.'),
        'Happiness Score List': ('http://127.0.0.1:8000/api/happinessscore/', 'GET: Endpoint to list happiness scores, POST: Endpoint to create a happiness score entry.'),
        # Add more endpoints with descriptions as needed
    }
    return render(request, 'api/index.html', {'routes': routes})

