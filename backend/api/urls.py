from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CountryViewSet, RegionViewSet, CountryRegionViewSet, EconomicDataViewSet, YearViewSet, SocialSupportDataViewSet, HealthDataViewSet, HappinessScoreViewSet, FreedomDataViewSet, GovernmentTrustDataViewSet, GenerosityDataViewSet

# This was written with reference to the following site
# https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358

# DRF のルーターインスタンスを作成
router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'countryregions', CountryRegionViewSet)
router.register(r'economicdata', EconomicDataViewSet)
router.register(r'years', YearViewSet)
router.register(r'socialsupportdata', SocialSupportDataViewSet)
router.register(r'healthdata', HealthDataViewSet)
router.register(r'happinessscore', HappinessScoreViewSet)
router.register(r'freedomdata', FreedomDataViewSet)
router.register(r'governmenttrust', GovernmentTrustDataViewSet)
router.register(r'generosity', GenerosityDataViewSet)

# regionsのURLパターンを追加
urlpatterns = [
    path('token/', views.WorldHappinessTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', include(router.urls)),
    path('', views.getRoutes, name='api-overview'),
]
