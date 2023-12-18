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
    """
    retrieve:
    Return the details of a specific country by its ID.

    list:
    Return a list of all countries.
    
    create:
    Create a new country entry.
    
    update:
    Update an existing country identified by its ID.

    partial_update:
    Partially update details of an existing country identified by its ID.

    destroy:
    Delete a specific country by its ID.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class RegionViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific region by its ID.

    list:
    Return a list of all regions.
    
    create:
    Create a new region entry.
    
    update:
    Update an existing region identified by its ID.

    partial_update:
    Partially update details of an existing region identified by its ID.

    destroy:
    Delete a specific region by its ID.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]

class CountryRegionViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific countryregion by its ID.

    list:
    Return a list of all countryregions.
    
    create:
    Create a new countryregion entry.
    
    update:
    Update an existing countryregion identified by its ID.

    partial_update:
    Partially update details of an existing countryregion identified by its ID.

    destroy:
    Delete a specific countryregion by its ID.
    """
    queryset = CountryRegion.objects.all()
    serializer_class = CountryRegionSerializer
    permission_classes = [IsAuthenticated]

class YearViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific year by its ID.

    list:
    Return a list of all years.
    
    create:
    Create a new year entry.
    
    update:
    Update an existing year identified by its ID.

    partial_update:
    Partially year details of an existing country identified by its ID.

    destroy:
    Delete a specific year by its ID.
    """
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [IsAuthenticated]

class EconomicDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific economic data by its ID.

    list:
    Return a list of all economic data.
    
    create:
    Create a new economic data entry.
    
    update:
    Update an existing economic data identified by its ID.

    partial_update:
    Partially update details of an existing economic data identified by its ID.

    destroy:
    Delete a specific economic data by its ID.
    """
    queryset = EconomicData.objects.all()
    serializer_class = EconomicDataSerializer
    permission_classes = [IsAuthenticated]

class SocialSupportDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific social support data by its ID.

    list:
    Return a list of all social support data.
    
    create:
    Create a new social support entry.
    
    update:
    Update an existing social support data identified by its ID.

    partial_update:
    Partially update details of an existing social support data identified by its ID.

    destroy:
    Delete a specific social support data by its ID.
    """
    queryset = SocialSupportData.objects.all()
    serializer_class = SocialSupportDataSerializer
    permission_classes = [IsAuthenticated]

class HealthDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific health data by its ID.

    list:
    Return a list of all health data.
    
    create:
    Create a new health data entry.
    
    update:
    Update an existing health data identified by its ID.

    partial_update:
    Partially update details of an existing health data identified by its ID.

    destroy:
    Delete a specific health data by its ID.
    """
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    permission_classes = [IsAuthenticated]
    
class FreedomDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific freedom data by its ID.

    list:
    Return a list of all freedom data.
    
    create:
    Create a new freedom data entry.
    
    update:
    Update an existing freedom data identified by its ID.

    partial_update:
    Partially update details of an existing freedom data identified by its ID.

    destroy:
    Delete a specific freedom data by its ID.
    """
    queryset = FreedomData.objects.all()
    serializer_class = FreedomDataSerializer
    permission_classes = [IsAuthenticated]

class HappinessScoreViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific happiness score by its ID.

    list:
    Return a list of all happiness score.
    
    create:
    Create a new happiness score entry.
    
    update:
    Update an existing happiness score identified by its ID.

    partial_update:
    Partially update details of an existing happiness score identified by its ID.

    destroy:
    Delete a specific happiness score by its ID.
    """
    queryset = HappinessScore.objects.all()
    serializer_class = HappinessScoreSerializer
    permission_classes = [IsAuthenticated]
    
class GovernmentTrustDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific government trust data by its ID.

    list:
    Return a list of all government trust data.
    
    create:
    Create a new government trust data entry.
    
    update:
    Update an existing government trust data identified by its ID.

    partial_update:
    Partially update details of an existing government trust data identified by its ID.

    destroy:
    Delete a specific government trust data by its ID.
    """
    queryset = GovernmentTrustData.objects.all()
    serializer_class = GovernmentTrustDataSerializer
    permission_classes = [IsAuthenticated]
    
class GenerosityDataViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the details of a specific generosity data by its ID.

    list:
    Return a list of all generosity data.
    
    create:
    Create a new generosity data entry.
    
    update:
    Update an existing generosity data identified by its ID.

    partial_update:
    Partially update details of an existing generosity data identified by its ID.

    destroy:
    Delete a specific generosity data by its ID.
    """
    queryset = GenerosityData.objects.all()
    serializer_class = GenerosityDataSerializer
    permission_classes = [IsAuthenticated]