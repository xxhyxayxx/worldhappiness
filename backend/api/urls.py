from django.urls import path
from django.views.generic import RedirectView
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Redirect index to swagger to display API information
    path('', RedirectView.as_view(url='/swagger/', permanent=True), name='index'),
    
    # JWT Token
    path('token/', views.WorldHappinessTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Register
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    
    # CountryViewSet
    path('country/', views.CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('country/<int:pk>/', views.CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='country-detail'),
    
    # RegionViewSet
    path('region/', views.RegionViewSet.as_view({'get': 'list', 'post': 'create'}), name='region-list'),
    path('region/<int:pk>/', views.RegionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='region-detail'),

    # CountryRegionViewSet
    path('countryregion/', views.CountryRegionViewSet.as_view({'get': 'list', 'post': 'create'}), name='countryregion-list'),
    path('countryregion/<int:pk>/', views.CountryRegionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='countryregion-detail'),
    
    # EconomicDataViewSet
    path('economicdata/', views.EconomicDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='economicdata-list'),
    path('economicdata/<int:pk>/', views.EconomicDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='economicdata-detail'),

    # YearViewSet
    path('years/', views.YearViewSet.as_view({'get': 'list', 'post': 'create'}), name='year-list'),
    path('year/<int:pk>/', views.YearViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='year-detail'),
    
    # SocialSupportDataViewSet
    path('socialsupportdata/', views.SocialSupportDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='socialsupportdata-list'),
    path('socialsupportdata/<int:pk>/', views.SocialSupportDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='socialsupportdata-detail'),

    # HealthDataViewSet
    path('healthdata/', views.HealthDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='healthdata-list'),
    path('healthdata/<int:pk>/', views.HealthDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='healthdata-detail'),

    # HappinessScoreViewSet
    path('happinessscore/', views.HappinessScoreViewSet.as_view({'get': 'list', 'post': 'create'}), name='happinessscore-list'),
    path('happinessscore/<int:pk>/', views.HappinessScoreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='happinessscore-detail'),

    # FreedomDataViewSet
    path('freedomdata/', views.FreedomDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='freedomdata-list'),
    path('freedomdata/<int:pk>/', views.FreedomDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='freedomdata-detail'),

    # GovernmentTrustDataViewSet
    path('governmenttrust/', views.GovernmentTrustDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='governmenttrustdata-list'),
    path('governmenttrust/<int:pk>/', views.GovernmentTrustDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='governmenttrustdata-detail'),

    # GenerosityDataViewSet
    path('generosity/', views.GenerosityDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='generositydata-list'),
    path('generosity/<int:pk>/', views.GenerosityDataViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='generositydata-detail'),

]

