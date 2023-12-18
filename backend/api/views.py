from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.serializers import WorldHappinessTokenObtainPairSerializer, RegisterSerializer, CountrySerializer, RegionSerializer, CountryRegionSerializer, EconomicDataSerializer, YearSerializer, SocialSupportDataSerializer, HealthDataSerializer, HappinessScoreSerializer, FreedomDataSerializer, GovernmentTrustDataSerializer, GenerosityDataSerializer
from .models import Country, Region, CountryRegion, EconomicData, Year, SocialSupportData, HealthData, HappinessScore, FreedomData, GovernmentTrustData, GenerosityData
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

# WorldHappinessTokenObtainPairView was written with reference to the following site
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358
class WorldHappinessTokenObtainPairView(TokenObtainPairView):
    """
    post:
    An endpoint for obtaining a pair of tokens.
    Provide a username and password and an access token and a refresh token will be returned.
    """
    serializer_class = WorldHappinessTokenObtainPairSerializer

# RegisterView was written with reference to the following site
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358
class RegisterView(generics.CreateAPIView):
    """
    post:
    Endpoint for registering new users.
    A username, email address, and password must be provided.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

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

def show_index(request):
    return render(request, 'api/index.html')