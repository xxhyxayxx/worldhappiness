from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    regions = models.ManyToManyField('Region', through='CountryRegion')
    
    # It is defined to represent model instances as strings in a human readable format.
    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100)
    
    # It is defined to represent model instances as strings in a human readable format.
    def __str__(self):
        return self.name

class CountryRegion(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Year(models.Model):
    year = models.IntegerField()
    
    # It is defined to represent model instances as strings in a human readable format.
    def __str__(self):
        return str(self.year)

# Create abstract base class with common fields
class CommonFields(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

# EconomicData
class EconomicData(CommonFields):
    gdp = models.DecimalField(max_digits=10, decimal_places=3)

# SocialSupportData
class SocialSupportData(CommonFields):
    social_support = models.DecimalField(max_digits=10, decimal_places=3)

# HealthData
class HealthData(CommonFields):
    life_expectancy = models.DecimalField(max_digits=10, decimal_places=3)

# FreedomData
class FreedomData(CommonFields):
    freedom = models.DecimalField(max_digits=10, decimal_places=3)

# GenerosityData
class GenerosityData(CommonFields):
    generosity = models.DecimalField(max_digits=10, decimal_places=3)

# GovernmentTrustData
class GovernmentTrustData(CommonFields):
    government_trust = models.DecimalField(max_digits=10, decimal_places=3)

# HappinessScore
class HappinessScore(CommonFields):
    happiness_score = models.DecimalField(max_digits=10, decimal_places=3)
