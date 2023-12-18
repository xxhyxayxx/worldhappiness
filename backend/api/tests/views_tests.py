from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Region, Country, CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, HappinessScore, GovernmentTrustData, GenerosityData
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from decimal import Decimal

class BaseTestCase(APITestCase):
    def setUp(self):
        # Create a test user in the database
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Generate a refresh token for the user, used for authentication
        refresh = RefreshToken.for_user(self.user)
        # Set the credentials for the client, adding the generated access token for authentication
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')


class CountryViewSetTestCase(BaseTestCase):
    def test_create_country(self):
        # Test creating a new country via a POST request
        url = reverse('country-list')
        data = {"name": "Test Country"}
        response = self.client.post(url, data)
        # Assert successful country creation and validate the country's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, "Test Country")

    def test_list_countries(self):
        # Test retrieving a list of countries via a GET request
        Country.objects.create(name="Country 1")
        url = reverse('country-list')
        response = self.client.get(url)
        # Assert successful retrieval and correct number of countries
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_country(self):
        # Test deleting a country via a DELETE request
        country = Country.objects.create(name="Country to Delete")
        url = reverse('country-detail', kwargs={'pk': country.pk})
        response = self.client.delete(url)
        # Assert successful deletion and check if the country count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Country.objects.count(), 0)


# RegionViewSetTestCase
class RegionViewSetTestCase(BaseTestCase):
    def test_create_region(self):
        # Test creating a new region via a POST request
        url = reverse('region-list')
        data = {"name": "Test Region"}
        response = self.client.post(url, data)
        # Assert successful region creation and validate the region's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), 1)
        self.assertEqual(Region.objects.get().name, "Test Region")

    def test_read_region(self):
        # Test reading a specific region's details via a GET request
        region = Region.objects.create(name="Test Region")
        url = reverse('region-detail', kwargs={'pk': region.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct region details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], region.name)

    def test_update_region(self):
        # Test updating a region's details via a PUT request
        region = Region.objects.create(name="Old Region")
        url = reverse('region-detail', kwargs={'pk': region.id})
        data = {"name": "Updated Region"}
        response = self.client.put(url, data)
        # Assert successful update and validate the updated region's name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        region.refresh_from_db()
        self.assertEqual(region.name, "Updated Region")

    def test_delete_region(self):
        # Test deleting a region via a DELETE request
        region = Region.objects.create(name="Region to Delete")
        url = reverse('region-detail', kwargs={'pk': region.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the region count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Region.objects.count(), 0)


class CountryRegionViewSetTestCase(BaseTestCase):
    def setUp(self):
        # Additional setup for country-region associations
        super().setUp()
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)

    def test_create_country_region(self):
        # Test creating a new country-region association via a POST request
        url = reverse('countryregion-list')
        data = {
            'country_id': self.country.id,
            'region_id': self.region.id
        }
        response = self.client.post(url, data)
        # Assert successful creation of the association
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_country_region(self):
        # Test reading details of a specific country-region association via a GET request
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct association details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['country'], self.country.name)  
        self.assertEqual(response.data['region'], self.region.name)
        
    def test_update_country_region(self):
        # Test updating a country-region association via a PUT request
        new_region = Region.objects.create(name="New Test Region")
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        data = {"country_id": self.country.id, "region_id": new_region.id}
        response = self.client.put(url, data)
        # Assert successful update and validate the updated association
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.country_region.refresh_from_db()
        self.assertEqual(self.country_region.region, new_region)

    def test_delete_country_region(self):
        # Test deleting a country-region association via a DELETE request
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the association count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CountryRegion.objects.count(), 0)


class YearViewSetTestCase(BaseTestCase):
    def test_create_year(self):
        # Test creating a new year entity via a POST request
        url = reverse('year-list')
        data = {'year': 2020}
        response = self.client.post(url, data)
        # Assert successful year creation and validate the year's value
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Year.objects.count(), 1)
        self.assertEqual(Year.objects.get().year, 2020)

    def test_read_year(self):
        # Test reading details of a specific year via a GET request
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct year value
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['year'], year.year)

    def test_update_year(self):
        # Test updating a year's value via a PUT request
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        data = {'year': 2021}
        response = self.client.put(url, data)
        # Assert successful update and validate the updated year value
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        year.refresh_from_db()
        self.assertEqual(year.year, 2021)

    def test_delete_year(self):
        # Test deleting a year entity via a DELETE request
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the year count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Year.objects.count(), 0)


class CommonDataTestCase(BaseTestCase):
    def setUp(self):
        # Calls the setUp of BaseTestCase for common setup
        super().setUp()
        # Create common test data for country, region, country-region association, and year
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        self.year = Year.objects.create(year=2020)


class EconomicDataViewSetTestCase(CommonDataTestCase):
    def test_create_economic_data(self):
        # Test creating new economic data via a POST request
        url = reverse('economicdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the economic data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EconomicData.objects.count(), 1)
        self.assertEqual(EconomicData.objects.get().gdp, Decimal('123.45'))

    def test_read_economic_data(self):
        # Test reading details of specific economic data via a GET request
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct economic data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['gdp'], '123.450')

    def test_update_economic_data(self):
        # Test updating economic data via a PUT request
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': 678.90
        }
        response = self.client.put(url, data)
        # Assertion for response status could be added here

    def test_delete_economic_data(self):
        # Test deleting economic data via a DELETE request
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the economic data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EconomicData.objects.count(), 0)


class SocialSupportDataViewSetTestCase(CommonDataTestCase):    
    def test_create_social_support_data(self):
        # Test creating new social support data via a POST request
        url = reverse('socialsupportdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the social support data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialSupportData.objects.count(), 1)
        self.assertEqual(SocialSupportData.objects.get().social_support, Decimal('123.45'))
    
    def test_read_social_support_data(self):
        # Test reading details of specific social support data via a GET request
        social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=123.45)
        url = reverse('socialsupportdata-detail', kwargs={'pk': social_support_data.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct social support data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['social_support'], '123.450')
    
    def test_delete_social_support_data(self):
        # Test deleting social support data via a DELETE request
        social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=123.45)
        url = reverse('socialsupportdata-detail', kwargs={'pk': social_support_data.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the social support data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SocialSupportData.objects.count(), 0)


class HealthDataViewSetTestCase(CommonDataTestCase):    
    def test_create_health_data(self):
        # Test creating new health data via a POST request
        url = reverse('healthdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the health data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HealthData.objects.count(), 1)
        self.assertEqual(HealthData.objects.get().life_expectancy, Decimal('123.45'))
    
    def test_read_health_data(self):
        # Test reading details of specific health data via a GET request
        health_data = HealthData.objects.create(country_region=self.country_region, year=self.year, life_expectancy=123.45)
        url = reverse('healthdata-detail', kwargs={'pk': health_data.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct health data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['life_expectancy'], '123.450')
    
    def test_delete_health_data(self):
        # Test deleting health data via a DELETE request
        health_data = HealthData.objects.create(country_region=self.country_region, year=self.year, life_expectancy=123.45)
        url = reverse('healthdata-detail', kwargs={'pk': health_data.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the health data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HealthData.objects.count(), 0)


class FreedomDataViewSetTestCase(CommonDataTestCase):    
    def test_create_freedom_data(self):
        # Test creating new freedom data via a POST request
        url = reverse('freedomdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the freedom data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FreedomData.objects.count(), 1)
        self.assertEqual(FreedomData.objects.get().freedom, Decimal('123.45'))
    
    def test_read_freedom_data(self):
        # Test reading details of specific freedom data via a GET request
        freedom_data = FreedomData.objects.create(country_region=self.country_region, year=self.year, freedom=123.45)
        url = reverse('freedomdata-detail', kwargs={'pk': freedom_data.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct freedom data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['freedom'], '123.450')
    
    def test_delete_freedom_data(self):
        # Test deleting freedom data via a DELETE request
        freedom_data = FreedomData.objects.create(country_region=self.country_region, year=self.year, freedom=123.45)
        url = reverse('freedomdata-detail', kwargs={'pk': freedom_data.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the freedom data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FreedomData.objects.count(), 0)


class HappinessScoreViewSetTestCase(CommonDataTestCase):    
    def test_create_happiness_score(self):
        # Test creating new happiness score data via a POST request
        url = reverse('happinessscore-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the happiness score's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HappinessScore.objects.count(), 1)
        self.assertEqual(HappinessScore.objects.get().happiness_score, Decimal('123.45'))
    
    def test_read_happiness_score(self):
        # Test reading details of specific happiness score data via a GET request
        happiness_score = HappinessScore.objects.create(country_region=self.country_region, year=self.year, happiness_score=123.45)
        url = reverse('happinessscore-detail', kwargs={'pk': happiness_score.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct happiness score details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['happiness_score'], '123.450')
    
    def test_delete_happiness_score(self):
        # Test deleting happiness score data via a DELETE request
        happiness_score = HappinessScore.objects.create(country_region=self.country_region, year=self.year, happiness_score=123.45)
        url = reverse('happinessscore-detail', kwargs={'pk': happiness_score.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the happiness score count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HappinessScore.objects.count(), 0)


class GovernmentTrustDataViewSetTestCase(CommonDataTestCase):    
    def test_create_government_trust_data(self):
        # Test creating new government trust data via a POST request
        url = reverse('governmenttrustdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the government trust data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GovernmentTrustData.objects.count(), 1)
        self.assertEqual(GovernmentTrustData.objects.get().government_trust, Decimal('123.45'))
    
    def test_read_government_trust_data(self):
        # Test reading details of specific government trust data via a GET request
        government_trust = GovernmentTrustData.objects.create(country_region=self.country_region, year=self.year, government_trust=123.45)
        url = reverse('governmenttrustdata-detail', kwargs={'pk': government_trust.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct government trust data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['government_trust'], '123.450')
    
    def test_delete_government_trust_data(self):
        # Test deleting government trust data via a DELETE request
        government_trust = GovernmentTrustData.objects.create(country_region=self.country_region, year=self.year, government_trust=123.45)
        url = reverse('governmenttrustdata-detail', kwargs={'pk': government_trust.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the government trust data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GovernmentTrustData.objects.count(), 0)


class GenerosityDataViewSetTestCase(CommonDataTestCase):    
    def test_create_generosity_data(self):
        # Test creating new generosity data via a POST request
        url = reverse('generositydata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 123.45
        }
        response = self.client.post(url, data)
        # Assert successful creation and validate the generosity data's properties
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GenerosityData.objects.count(), 1)
        self.assertEqual(GenerosityData.objects.get().generosity, Decimal('123.45'))
    
    def test_read_generosity_data(self):
        # Test reading details of specific generosity data via a GET request
        generosity = GenerosityData.objects.create(country_region=self.country_region, year=self.year, generosity=123.45)
        url = reverse('generositydata-detail', kwargs={'pk': generosity.id})
        response = self.client.get(url)
        # Assert successful retrieval and correct generosity data details
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['generosity'], '123.450')
    
    def test_delete_generosity_data(self):
        # Test deleting generosity data via a DELETE request
        generosity = GenerosityData.objects.create(country_region=self.country_region, year=self.year, generosity=123.45)
        url = reverse('generositydata-detail', kwargs={'pk': generosity.id})
        response = self.client.delete(url)
        # Assert successful deletion and check if the generosity data count is zero
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GenerosityData.objects.count(), 0)
