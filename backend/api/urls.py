from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CountryViewSet, RegionViewSet, CountryRegionViewSet, EconomicDataViewSet, YearViewSet, SocialSupportDataViewSet, HealthDataViewSet

# DRF のルーターインスタンスを作成
router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'countryregions', CountryRegionViewSet)
router.register(r'economicdata', EconomicDataViewSet)
router.register(r'years', YearViewSet)
router.register(r'socialsupportdata', SocialSupportDataViewSet)
router.register(r'healthdata', HealthDataViewSet)

urlpatterns = [
    path('token/', views.WorldHappinessTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(),name='auth_register'),
    path('', include(router.urls)),
    path('', views.getRoutes),
]