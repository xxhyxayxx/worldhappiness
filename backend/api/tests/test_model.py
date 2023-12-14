from django.test import TestCase
from api.models import Country, Region, CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, GenerosityData, GovernmentTrustData, HappinessScore

class ModelsTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        self.year = Year.objects.create(year=2020)

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Test Country")

    def test_region_creation(self):
        self.assertEqual(self.region.name, "Test Region")

    def test_country_region_creation(self):
        self.assertEqual(self.country_region.country, self.country)
        self.assertEqual(self.country_region.region, self.region)

    def test_year_creation(self):
        self.assertEqual(self.year.year, 2020)

    def test_economic_data_creation(self):
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=12345.678)
        self.assertEqual(economic_data.gdp, 12345.678)

    def test_social_support_data_creation(self):
        social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=5.432)
        self.assertEqual(social_support_data.social_support, 5.432)

    def test_health_data_creation(self):
        health_data = HealthData.objects.create(country_region=self.country_region, year=self.year, life_expectancy=70.5)
        self.assertEqual(health_data.life_expectancy, 70.5)

    def test_freedom_data_creation(self):
        freedom_data = FreedomData.objects.create(country_region=self.country_region, year=self.year, freedom=0.876)
        self.assertEqual(freedom_data.freedom, 0.876)

    def test_generosity_data_creation(self):
        generosity_data = GenerosityData.objects.create(country_region=self.country_region, year=self.year, generosity=0.321)
        self.assertEqual(generosity_data.generosity, 0.321)

    def test_government_trust_data_creation(self):
        government_trust_data = GovernmentTrustData.objects.create(country_region=self.country_region, year=self.year, government_trust=0.654)
        self.assertEqual(government_trust_data.government_trust, 0.654)

    def test_happiness_score_creation(self):
        happiness_score = HappinessScore.objects.create(country_region=self.country_region, year=self.year, happiness_score=7.89)
        self.assertEqual(happiness_score.happiness_score, 7.89)
