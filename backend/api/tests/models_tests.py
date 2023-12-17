from django.test import TestCase
from api.models import Country, Region, CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, GenerosityData, GovernmentTrustData, HappinessScore
import random
from decimal import Decimal

class CountryModelTestCase(TestCase):
    def test_create_country(self):
        # Create a new country and save it to the database
        country = Country.objects.create(name="Test Country")
        
        # Check that the country is saved in the database
        self.assertEqual(Country.objects.count(), 1)
        
        # Verify that the name of the created country is correct
        self.assertEqual(country.name, "Test Country")

    def test_country_str(self):
        # Ensure the string representation of the country is correct
        country = Country.objects.create(name="Test Country")
        self.assertEqual(str(country), "Test Country")

    def test_add_region_to_country(self):
        # Check if a region can be added to a country
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        
        country.regions.add(region)
        
        self.assertEqual(country.regions.count(), 1)


class RegionModelTestCase(TestCase):
    def test_create_region(self):
        # Create a new region and save it to the database
        region = Region.objects.create(name="Test Region")
        
        # Check that the region is saved in the database
        self.assertEqual(Region.objects.count(), 1)
        
        # Verify that the name of the created region is correct
        self.assertEqual(region.name, "Test Region")

    def test_region_str(self):
        # Ensure the string representation of the region is correct
        region = Region.objects.create(name="Test Region")
        self.assertEqual(str(region), "Test Region")


class CountryRegionModelTestCase(TestCase):
    def setUp(self):
        # Create instances of Country and Region for testing
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")

    def test_create_country_region(self):
        # Create a new CountryRegion and save it to the database
        country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        
        # Check that the countryRegion is saved in the database
        self.assertEqual(CountryRegion.objects.count(), 1)
        
        # Verify that the CountryRegion associations you created are correct
        self.assertEqual(country_region.country, self.country)
        self.assertEqual(country_region.region, self.region)

    def test_cascade_deletion(self):
        # Create CountryRegion
        country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        
        # Delet the Country
        self.country.delete()
        
        # Make sure CountryRegion is also deleted
        self.assertEqual(CountryRegion.objects.count(), 0)

class CommonFieldsModelTestCase(TestCase):
    def setUp(self):
        # Create Country and Region
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")

        # Create CountryRegion and Year
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        self.year = Year.objects.create(year=random.randint(2000, 2023))
        
    def test_create_economic_data(self):
        # Set random values in EconomicData model
        self.gdp = Decimal(random.uniform(1000, 100000))
        
        # Create EconomicData model
        economic_data = EconomicData.objects.create(
            country_region=self.country_region,
            year=self.year,
            gdp=self.gdp
        )

        # Check the Economic data is saved in the database
        self.assertEqual(EconomicData.objects.count(), 1)
        self.assertEqual(economic_data.country_region, self.country_region)
        self.assertEqual(economic_data.year, self.year)
        self.assertEqual(economic_data.gdp, self.gdp) 
    
    def test_social_support_data(self):
        # Set random values in Social Support model
        self.social_support = Decimal(random.uniform(1000, 100000))
        
        # Create SocialSupport Data model
        social_support_data = SocialSupportData.objects.create(
            country_region=self.country_region,
            year=self.year,
            social_support=self.social_support
        )

        # Check the Social Support data is saved in the database
        self.assertEqual(SocialSupportData.objects.count(), 1)
        self.assertEqual(social_support_data.country_region, self.country_region)
        self.assertEqual(social_support_data.year, self.year)
        self.assertEqual(social_support_data.social_support, self.social_support) 
        
    def test_health_data(self):
        # Set random values in Health model
        self.life_expectancy = Decimal(random.uniform(1000, 100000))
        
        # Create Health Data model
        health_data = HealthData.objects.create(
            country_region=self.country_region,
            year=self.year,
            life_expectancy=self.life_expectancy
        )

        # Check the Health data is saved in the database
        self.assertEqual(HealthData.objects.count(), 1)
        self.assertEqual(health_data.country_region, self.country_region)
        self.assertEqual(health_data.year, self.year)
        self.assertEqual(health_data.life_expectancy, self.life_expectancy) 
    
    def test_happiness_score(self):
        # Set random values in Happiness Score model
        self.happiness_score = Decimal(random.uniform(1000, 100000))
        
        # Create Happiness Score model
        happiness_score = HappinessScore.objects.create(
            country_region=self.country_region,
            year=self.year,
            happiness_score=self.happiness_score
        )

        # Check the Happiness Score data is saved in the database
        self.assertEqual(HappinessScore.objects.count(), 1)
        self.assertEqual(happiness_score.country_region, self.country_region)
        self.assertEqual(happiness_score.year, self.year)
        self.assertEqual(happiness_score.happiness_score, self.happiness_score)
    
    def test_freedom_data(self):
        # Set random values in Freedom Data model
        self.freedom = Decimal(random.uniform(1000, 100000))
        
        # Create Freedom Data model
        freedom_data = FreedomData.objects.create(
            country_region=self.country_region,
            year=self.year,
            freedom=self.freedom
        )

        # Check the Freedom data is saved in the database
        self.assertEqual(FreedomData.objects.count(), 1)
        self.assertEqual(freedom_data.country_region, self.country_region)
        self.assertEqual(freedom_data.year, self.year)
        self.assertEqual(freedom_data.freedom, self.freedom)  
    
    def test_generosity_data(self):
        # Set random values in Generosity Data model
        self.generosity = Decimal(random.uniform(1000, 100000))
        
        # Create Generosity Data model
        generosity_data = GenerosityData.objects.create(
            country_region=self.country_region,
            year=self.year,
            generosity=self.generosity
        )

        # Check the Generosity data is saved in the database
        self.assertEqual(GenerosityData.objects.count(), 1)
        self.assertEqual(generosity_data.country_region, self.country_region)
        self.assertEqual(generosity_data.year, self.year)
        self.assertEqual(generosity_data.generosity, self.generosity) 
    
    def test_government_trust_data(self):
        # Set random values in Government Trust Data model
        self.government_trust = Decimal(random.uniform(1000, 100000))
        
        # Create Government Trust Data model
        government_trust_data = GovernmentTrustData.objects.create(
            country_region=self.country_region,
            year=self.year,
            government_trust=self.government_trust
        )

        # Check the Government Trust data is saved in the database
        self.assertEqual(GovernmentTrustData.objects.count(), 1)
        self.assertEqual(government_trust_data.country_region, self.country_region)
        self.assertEqual(government_trust_data.year, self.year)
        self.assertEqual(government_trust_data.government_trust, self.government_trust)  

    