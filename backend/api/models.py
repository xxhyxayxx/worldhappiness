from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    regions = models.ManyToManyField('Region', through='CountryRegion')
    
    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CountryRegion(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Year(models.Model):
    year = models.IntegerField()
    
    def __str__(self):
        return str(self.year)

class EconomicData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    gdp = models.DecimalField(max_digits=10, decimal_places=3)
    
class SocialSupportData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    social_support = models.DecimalField(max_digits=10, decimal_places=3)

class HealthData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    life_expectancy = models.DecimalField(max_digits=10, decimal_places=3)

class FreedomData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    freedom = models.DecimalField(max_digits=10, decimal_places=3)

class GenerosityData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    generosity = models.DecimalField(max_digits=10, decimal_places=3)

class GovernmentTrustData(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    government_trust = models.DecimalField(max_digits=10, decimal_places=3)

class HappinessScore(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    happiness_score = models.DecimalField(max_digits=10, decimal_places=3)

