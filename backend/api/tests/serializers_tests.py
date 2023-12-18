from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Region, Country, Year, EconomicData, CountryRegion, SocialSupportData, HealthData, FreedomData, HappinessScore, GovernmentTrustData, GenerosityData
from django.contrib.auth.models import User
from decimal import Decimal

class BaseTestCase(TestCase):
    # setUp is called before each test method
    def setUp(self):
        self.client = APIClient()  # Initializes the API client
        # User data for creating a test user
        self.user_data = {
            "username": "testuser",
            "password": "testpassword",
        }
        # Create a test user in the database
        self.user = User.objects.create_user(**self.user_data)
        # Authenticate the user and retrieve the access token
        self.login_response = self.client.post('/api/token/', self.user_data)
        self.access_token = self.login_response.data["access"]
        # Set the authorization header for subsequent requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

class RegionSerializerTestCase(BaseTestCase):
    # Test the creation of a region
    def test_create_region(self):
        data = {"name": "Test Region"}
        # POST request to create a new region
        response = self.client.post('/api/region/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if creation was successful
        self.assertEqual(Region.objects.count(), 1)  # Ensure one region is in the database
        self.assertEqual(Region.objects.get().name, "Test Region")  # Verify the region's name

    # Test the update of an existing region
    def test_update_region(self):
        region = Region.objects.create(name="Old Region")
        data = {"name": "New Region"}
        # PUT request to update the region
        response = self.client.put(f'/api/region/{region.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if update was successful
        self.assertEqual(Region.objects.get(id=region.id).name, "New Region")  # Verify the updated region's name

    # Test the update of a nonexistent region
    def test_update_nonexistent_region(self):
        data = {"name": "New Region"}
        # PUT request to update a region that doesn't exist
        response = self.client.put('/api/region/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Check if the correct status code is returned

class CountrySerializerTestCase(BaseTestCase):
    # Test the creation of a country
    def test_create_country(self):
        data = {"name": "Test Country"}
        # POST request to create a new country
        response = self.client.post('/api/country/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if creation was successful
        self.assertEqual(Country.objects.count(), 1)  # Ensure one country is in the database
        self.assertEqual(Country.objects.get().name, "Test Country")  # Verify the country's name

    # Test the update of an existing country
    def test_update_country(self):
        country = Country.objects.create(name="Old Country")
        data = {"name": "New Country"}
        # PUT request to update the country
        response = self.client.put(f'/api/country/{country.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if update was successful
        self.assertEqual(Country.objects.get(id=country.id).name, "New Country")  # Verify the updated country's name

    # Test the update of a nonexistent country
    def test_update_nonexistent_country(self):
        data = {"name": "New Country"}
        # PUT request to update a country that doesn't exist
        response = self.client.put('/api/country/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Check if the correct status code is returned

    # Test associating a region to a country during creation
    def test_associate_region_to_country(self):
        region = Region.objects.create(name="Test Region")
        data = {"name": "Test Country", "region_id": region.id}
        # POST request to create a country and associate it with a region
        response = self.client.post('/api/country/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if creation was successful
        country = Country.objects.get(name="Test Country")
        self.assertEqual(country.regions.count(), 1)  # Ensure the country is associated with one region
        self.assertEqual(country.regions.first().name, "Test Region")  # Verify the associated region's name

    # Test creating a country with an invalid region association
    def test_invalid_association(self):
        data = {"name": "Test Country", "region_id": 999}
        # POST request to create a country with an invalid region id
        response = self.client.post('/api/country/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Check if the correct status code is returned
        self.assertIn("region_id", response.data)  # Check if the error is related to the region_id

class CountryRegionSerializerTestCase(BaseTestCase):
    # Set up data for the tests
    def setUp(self):
        super().setUp()  # Calls setUp of the base test case
        # Create a test country and region
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        # Create a country-region association for testing
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)

    # Test creating a new country-region association
    def test_create_country_region(self):
        data = {
            'country_id': self.country.id,
            'region_id': self.region.id
        }
        response = self.client.post('/api/countryregion/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CountryRegion.objects.count(), 2)  # Check the count of country-region pairs
        new_country_region = CountryRegion.objects.latest('id')
        self.assertEqual(new_country_region.country, self.country)
        self.assertEqual(new_country_region.region, self.region)

    # Test reading a specific country-region association
    def test_read_country_region(self):
        response = self.client.get(f'/api/countryregion/{self.country_region.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['country'], self.country.name)
        self.assertEqual(response.data['region'], self.region.name)

    # Test updating a country-region association
    def test_update_country_region(self):
        new_region = Region.objects.create(name="New Region")
        data = {
            'country_id': self.country.id,
            'region_id': new_region.id
        }
        response = self.client.put(f'/api/countryregion/{self.country_region.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_country_region = CountryRegion.objects.get(id=self.country_region.id)
        self.assertEqual(updated_country_region.region, new_region)

    # Test deleting a country-region association
    def test_delete_country_region(self):
        response = self.client.delete(f'/api/countryregion/{self.country_region.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CountryRegion.objects.filter(id=self.country_region.id).exists())

class YearSerializerTestCase(BaseTestCase):
    # Test creating a new year
    def test_create_year(self):
        data = {"year": 2020}
        response = self.client.post('/api/years/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Year.objects.count(), 1)
        self.assertEqual(Year.objects.get().year, 2020)

    # Test updating an existing year
    def test_update_year(self):
        year = Year.objects.create(year=2020)
        data = {"year": 2021}
        response = self.client.put(f'/api/year/{year.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Year.objects.get(id=year.id).year, 2021)

    # Test updating a nonexistent year
    def test_update_nonexistent_year(self):
        data = {"year": 2021}
        response = self.client.put('/api/year/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EconomicDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)

    # Test creating new economic data
    def test_create_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '123.45'
        }
        response = self.client.post('/api/economicdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing economic data
    def test_update_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '678.90'
        }
        response = self.client.put(f'/api/economicdata/{self.economic_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test updating non-existent economic data
    def test_update_nonexistent_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '456.78'
        }
        response = self.client.put('/api/economicdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SocialSupportDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=5.5)

    # Test creating new social support data
    def test_create_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 6.5
        }
        response = self.client.post('/api/socialsupportdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing social support data
    def test_update_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 7.5
        }
        response = self.client.put(f'/api/socialsupportdata/{self.social_support_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test updating non-existent social support data
    def test_update_nonexistent_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 8.5
        }
        response = self.client.put('/api/socialsupportdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class HealthDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.health_data = HealthData.objects.create(country_region=self.country_region, year=self.year, life_expectancy=70.0)

    # Test creating new health data
    def test_create_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 72.5
        }
        response = self.client.post('/api/healthdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing health data
    def test_update_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 75.0
        }
        response = self.client.put(f'/api/healthdata/{self.health_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test updating non-existent health data
    def test_update_nonexistent_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 80.0
        }
        response = self.client.put('/api/healthdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class FreedomDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.freedom_data = FreedomData.objects.create(country_region=self.country_region, year=self.year, freedom=0.8)

    # Test creating new freedom data
    def test_create_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 0.9
        }
        response = self.client.post('/api/freedomdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing freedom data
    def test_update_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 0.95
        }
        response = self.client.put(f'/api/freedomdata/{self.freedom_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test updating non-existent freedom data
    def test_update_nonexistent_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 1.0
        }
        response = self.client.put('/api/freedomdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class HappinessScoreSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.happiness_score_data = HappinessScore.objects.create(country_region=self.country_region, year=self.year, happiness_score=5.5)

    # Test creating new happiness score data
    def test_create_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 6.5
        }
        response = self.client.post('/api/happinessscore/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing happiness score data
    def test_update_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 7.5
        }
        response = self.client.put(f'/api/happinessscore/{self.happiness_score_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test updating non-existent happiness score data
    def test_update_nonexistent_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 8.5
        }
        response = self.client.put('/api/happinessscore/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GovernmentTrustDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.government_trust_data = GovernmentTrustData.objects.create(country_region=self.country_region, year=self.year, government_trust=0.5)

    # Test creating new government trust data
    def test_create_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.6
        }
        response = self.client.post('/api/governmenttrust/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GovernmentTrustData.objects.count(), 2)

    # Test updating existing government trust data
    def test_update_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.7
        }
        response = self.client.put(f'/api/governmenttrust/{self.government_trust_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = GovernmentTrustData.objects.get(id=self.government_trust_data.id)
        self.assertEqual(updated_data.government_trust, Decimal('0.7')) 
        
    # Test updating non-existent government data
    def test_update_nonexistent_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.8
        }
        response = self.client.put('/api/governmenttrust/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GenerosityDataSerializerTestCase(BaseTestCase):
    # Set up common data for all tests
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.generosity_data = GenerosityData.objects.create(country_region=self.country_region, year=self.year, generosity=0.5)

    # Test creating new generosity data
    def test_create_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.6
        }
        response = self.client.post('/api/generosity/', data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating existing generosity data
    def test_update_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.7
        }
        response = self.client.put(f'/api/generosity/{self.generosity_data.id}/', data)
        if response.status_code != status.HTTP_200_OK:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # Test updating non-existent generosity data
    def test_update_nonexistent_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.8
        }
        response = self.client.put('/api/generosity/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)