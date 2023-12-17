from django.contrib import admin
from api.models import Country, Region, CountryRegion, EconomicData, SocialSupportData, HealthData, HappinessScore, FreedomData, GovernmentTrustData, GenerosityData

# CountryとRegionをadminサイトに登録
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(EconomicData)
admin.site.register(CountryRegion)
admin.site.register(HappinessScore)
admin.site.register(SocialSupportData)
admin.site.register(HealthData)
admin.site.register(FreedomData)
admin.site.register(GovernmentTrustData)
admin.site.register(GenerosityData)

