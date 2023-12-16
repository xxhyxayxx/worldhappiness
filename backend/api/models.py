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

# 共通のフィールドを持つ抽象基底クラスを作成
class CommonFields(models.Model):
    country_region = models.ForeignKey(CountryRegion, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True  # このクラスを抽象基底クラスとしてマーク

# EconomicData モデル
class EconomicData(CommonFields):
    gdp = models.DecimalField(max_digits=10, decimal_places=3)

# SocialSupportData モデル
class SocialSupportData(CommonFields):
    social_support = models.DecimalField(max_digits=10, decimal_places=3)

# HealthData モデル
class HealthData(CommonFields):
    life_expectancy = models.DecimalField(max_digits=10, decimal_places=3)

# FreedomData モデル
class FreedomData(CommonFields):
    freedom = models.DecimalField(max_digits=10, decimal_places=3)

# GenerosityData モデル
class GenerosityData(CommonFields):
    generosity = models.DecimalField(max_digits=10, decimal_places=3)

# GovernmentTrustData モデル
class GovernmentTrustData(CommonFields):
    government_trust = models.DecimalField(max_digits=10, decimal_places=3)

# HappinessScore モデル
class HappinessScore(CommonFields):
    happiness_score = models.DecimalField(max_digits=10, decimal_places=3)
