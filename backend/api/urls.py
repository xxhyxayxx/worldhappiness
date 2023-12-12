from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CountryViewSet, RegionViewSet, CountryRegionViewSet, EconomicDataViewSet

# DRF のルーターインスタンスを作成
router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'countryregions', CountryRegionViewSet)
router.register(r'economicdata', EconomicDataViewSet)

urlpatterns = [
    path('token/', views.WorldHappinessTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', views.getRoutes)
]