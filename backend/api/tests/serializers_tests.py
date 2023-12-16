from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Region, Country, Year, EconomicData, CountryRegion, SocialSupportData, HealthData, FreedomData, HappinessScore, GovernmentTrustData, GenerosityData
from django.contrib.auth.models import User
from decimal import Decimal

class BaseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "password": "testpassword",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.login_response = self.client.post('/api/token/', self.user_data)
        self.access_token = self.login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

class RegionSerializerTestCase(BaseTestCase):
    def test_create_region(self):
        data = {"name": "Test Region"}
        response = self.client.post('/api/regions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), 1)
        self.assertEqual(Region.objects.get().name, "Test Region")

    def test_update_region(self):
        region = Region.objects.create(name="Old Region")
        data = {"name": "New Region"}
        response = self.client.put(f'/api/regions/{region.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Region.objects.get(id=region.id).name, "New Region")

    def test_update_nonexistent_region(self):
        data = {"name": "New Region"}
        response = self.client.put('/api/regions/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CountrySerializerTestCase(BaseTestCase):
    def test_create_country(self):
        data = {"name": "Test Country"}
        response = self.client.post('/api/countries/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, "Test Country")

    def test_update_country(self):
        country = Country.objects.create(name="Old Country")
        data = {"name": "New Country"}
        response = self.client.put(f'/api/countries/{country.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Country.objects.get(id=country.id).name, "New Country")

    def test_update_nonexistent_country(self):
        data = {"name": "New Country"}
        response = self.client.put('/api/countries/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_associate_region_to_country(self):
        region = Region.objects.create(name="Test Region")
        data = {"name": "Test Country", "region_id": region.id}
        response = self.client.post('/api/countries/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        country = Country.objects.get(name="Test Country")
        self.assertEqual(country.regions.count(), 1)
        self.assertEqual(country.regions.first().name, "Test Region")

    def test_invalid_association(self):
        data = {"name": "Test Country", "region_id": 999}
        response = self.client.post('/api/countries/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("region_id", response.data)

class CountryRegionSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)

    def test_create_country_region(self):
        data = {
            'country_id': self.country.id,
            'region_id': self.region.id
        }
        response = self.client.post('/api/countryregions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CountryRegion.objects.count(), 2)
        new_country_region = CountryRegion.objects.latest('id')
        self.assertEqual(new_country_region.country, self.country)
        self.assertEqual(new_country_region.region, self.region)

    def test_read_country_region(self):
        response = self.client.get(f'/api/countryregions/{self.country_region.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['country'], self.country.name)
        self.assertEqual(response.data['region'], self.region.name)

    def test_update_country_region(self):
        new_region = Region.objects.create(name="New Region")
        data = {
            'country_id': self.country.id,
            'region_id': new_region.id
        }
        response = self.client.put(f'/api/countryregions/{self.country_region.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_country_region = CountryRegion.objects.get(id=self.country_region.id)
        self.assertEqual(updated_country_region.region, new_region)

    def test_delete_country_region(self):
        response = self.client.delete(f'/api/countryregions/{self.country_region.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CountryRegion.objects.filter(id=self.country_region.id).exists())

class YearSerializerTestCase(BaseTestCase):
    def test_create_year(self):
        data = {"year": 2020}
        response = self.client.post('/api/years/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Year.objects.count(), 1)
        self.assertEqual(Year.objects.get().year, 2020)

    def test_update_year(self):
        year = Year.objects.create(year=2020)
        data = {"year": 2021}
        response = self.client.put(f'/api/years/{year.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Year.objects.get(id=year.id).year, 2021)

    def test_update_nonexistent_year(self):
        data = {"year": 2021}
        response = self.client.put('/api/years/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class EconomicDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)

    def test_create_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '123.45'  # 'gdp' フィールドを追加
        }
        response = self.client.post('/api/economicdata/', data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # エラーメッセージを出力
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '678.90'  # 'gdp' フィールドを更新
        }
        response = self.client.put(f'/api/economicdata/{self.economic_data.id}/', data)
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # エラーメッセージを出力
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_nonexistent_economic_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': '456.78'  # 'gdp' フィールドを使用
        }
        response = self.client.put('/api/economicdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class SocialSupportDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=5.5)

    def test_create_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 6.5
        }
        response = self.client.post('/api/socialsupportdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialSupportData.objects.count(), 2)  # 初期データ + 新規データ

    def test_update_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 7.5
        }
        response = self.client.put(f'/api/socialsupportdata/{self.social_support_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = SocialSupportData.objects.get(id=self.social_support_data.id)
        self.assertEqual(updated_data.social_support, 7.5)

    def test_update_nonexistent_social_support_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 8.5
        }
        response = self.client.put('/api/socialsupportdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class HealthDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.health_data = HealthData.objects.create(country_region=self.country_region, year=self.year, life_expectancy=70.0)

    def test_create_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 72.5
        }
        response = self.client.post('/api/healthdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HealthData.objects.count(), 2)  # 初期データ + 新規データ

    def test_update_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 75.0
        }
        response = self.client.put(f'/api/healthdata/{self.health_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = HealthData.objects.get(id=self.health_data.id)
        self.assertEqual(updated_data.life_expectancy, 75.0)

    def test_update_nonexistent_health_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'life_expectancy': 80.0
        }
        response = self.client.put('/api/healthdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class FreedomDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.freedom_data = FreedomData.objects.create(country_region=self.country_region, year=self.year, freedom=0.8)

    def test_create_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 0.9
        }
        response = self.client.post('/api/freedomdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FreedomData.objects.count(), 2)  # 初期データ + 新規データ

    def test_update_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 0.95
        }
        response = self.client.put(f'/api/freedomdata/{self.freedom_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = FreedomData.objects.get(id=self.freedom_data.id)
        self.assertEqual(updated_data.freedom, Decimal('0.95'))

    def test_update_nonexistent_freedom_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'freedom': 1.0
        }
        response = self.client.put('/api/freedomdata/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class HappinessScoreSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.happiness_score_data = HappinessScore.objects.create(country_region=self.country_region, year=self.year, happiness_score=5.5)

    def test_create_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 6.5
        }
        response = self.client.post('/api/happinessscore/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HappinessScore.objects.count(), 2)  # 初期データ + 新規データ

    def test_update_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 7.5
        }
        response = self.client.put(f'/api/happinessscore/{self.happiness_score_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = HappinessScore.objects.get(id=self.happiness_score_data.id)
        self.assertEqual(updated_data.happiness_score, Decimal('7.5'))  # Decimal オブジェクトで比較

    def test_update_nonexistent_happiness_score_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'happiness_score': 8.5
        }
        response = self.client.put('/api/happinessscore/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GovernmentTrustDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.government_trust_data = GovernmentTrustData.objects.create(country_region=self.country_region, year=self.year, government_trust=0.5)

    def test_create_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.6
        }
        response = self.client.post('/api/governmenttrust/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GovernmentTrustData.objects.count(), 2)  # 初期データ + 新規データ

    def test_update_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.7
        }
        response = self.client.put(f'/api/governmenttrust/{self.government_trust_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_data = GovernmentTrustData.objects.get(id=self.government_trust_data.id)
        self.assertEqual(updated_data.government_trust, Decimal('0.7'))  # Decimal オブジェクトで比較

    def test_update_nonexistent_government_trust_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'government_trust': 0.8
        }
        response = self.client.put('/api/governmenttrust/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GenerosityDataSerializerTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=country, region=region)
        self.year = Year.objects.create(year=2020)
        self.generosity_data = GenerosityData.objects.create(country_region=self.country_region, year=self.year, generosity=0.5)

    def test_create_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.6
        }
        response = self.client.post('/api/generosity/', data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # エラーメッセージを出力
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.7
        }
        response = self.client.put(f'/api/generosity/{self.generosity_data.id}/', data)
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # エラーメッセージを出力
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_nonexistent_generosity_data(self):
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'generosity': 0.8
        }
        response = self.client.put('/api/generosity/999/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)