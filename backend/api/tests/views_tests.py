from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Region, Country, CountryRegion, Year, EconomicData, SocialSupportData, HealthData
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from decimal import Decimal

class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

class CountryViewSetTestCase(BaseTestCase):
    def test_create_country(self):
        url = reverse('country-list')
        data = {"name": "Test Country"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, "Test Country")

    def test_list_countries(self):
        Country.objects.create(name="Country 1")
        url = reverse('country-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_country(self):
        country = Country.objects.create(name="Country to Delete")
        url = reverse('country-detail', kwargs={'pk': country.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Country.objects.count(), 0)

# RegionViewSetTestCase
class RegionViewSetTestCase(BaseTestCase):
    def test_create_region(self):
        url = reverse('region-list')
        data = {"name": "Test Region"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Region.objects.count(), 1)
        self.assertEqual(Region.objects.get().name, "Test Region")

    def test_read_region(self):
        region = Region.objects.create(name="Test Region")
        url = reverse('region-detail', kwargs={'pk': region.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], region.name)

    def test_update_region(self):
        region = Region.objects.create(name="Old Region")
        url = reverse('region-detail', kwargs={'pk': region.id})
        data = {"name": "Updated Region"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        region.refresh_from_db()
        self.assertEqual(region.name, "Updated Region")

    def test_delete_region(self):
        region = Region.objects.create(name="Region to Delete")
        url = reverse('region-detail', kwargs={'pk': region.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Region.objects.count(), 0)

class CountryRegionViewSetTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        # Country と Region インスタンスを作成
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        # CountryRegion インスタンスを作成
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)

    def test_create_country_region(self):
        url = reverse('countryregion-list')
        data = {
            'country_id': self.country.id,
            'region_id': self.region.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_country_region(self):
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['country'], self.country.name)  # 'country' フィールドの値を確認
        self.assertEqual(response.data['region'], self.region.name)  # 'region' フィールドの値を確認

    def test_update_country_region(self):
        new_region = Region.objects.create(name="New Test Region")
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        data = {"country_id": self.country.id, "region_id": new_region.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.country_region.refresh_from_db()
        self.assertEqual(self.country_region.region, new_region)

    def test_delete_country_region(self):
        url = reverse('countryregion-detail', kwargs={'pk': self.country_region.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CountryRegion.objects.count(), 0)

class YearViewSetTestCase(BaseTestCase):
    def test_create_year(self):
        url = reverse('year-list')
        data = {'year': 2020}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Year.objects.count(), 1)
        self.assertEqual(Year.objects.get().year, 2020)

    def test_read_year(self):
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['year'], year.year)

    def test_update_year(self):
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        data = {'year': 2021}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        year.refresh_from_db()
        self.assertEqual(year.year, 2021)

    def test_delete_year(self):
        year = Year.objects.create(year=2020)
        url = reverse('year-detail', kwargs={'pk': year.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Year.objects.count(), 0)

class CommonDataTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        # 共通データのセットアップ
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        self.year = Year.objects.create(year=2020)

class EconomicDataViewSetTestCase(CommonDataTestCase):
    def test_create_economic_data(self):
        url = reverse('economicdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'gdp': 123.45
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EconomicData.objects.count(), 1)
        self.assertEqual(EconomicData.objects.get().gdp, Decimal('123.45'))

    def test_read_economic_data(self):
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['gdp'], '123.450')

    def test_update_economic_data(self):
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        data = {
            'country_region_id': self.country_region.id,  # 必要に応じて追加
            'year_id': self.year.id,  # 必要に応じて追加
            'gdp': 678.90
        }
        response = self.client.put(url, data)

    def test_delete_economic_data(self):
        economic_data = EconomicData.objects.create(country_region=self.country_region, year=self.year, gdp=123.45)
        url = reverse('economicdata-detail', kwargs={'pk': economic_data.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EconomicData.objects.count(), 0)

class SocialSupportDataViewSetTestCase(CommonDataTestCase):    
    def test_create_social_support_data(self):
        url = reverse('socialsupportdata-list')
        data = {
            'country_region_id': self.country_region.id,
            'year_id': self.year.id,
            'social_support': 123.45
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialSupportData.objects.count(), 1)
        self.assertEqual(SocialSupportData.objects.get().social_support, Decimal('123.45'))
    
    def test_read_social_support_data(self):
        social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=123.45)
        url = reverse('socialsupportdata-detail', kwargs={'pk': social_support_data.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['social_support'], '123.450')
    
    def test_delete_social_support_data(self):
        social_support_data = SocialSupportData.objects.create(country_region=self.country_region, year=self.year, social_support=123.45)
        url = reverse('socialsupportdata-detail', kwargs={'pk': social_support_data.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SocialSupportData.objects.count(), 0)
    
    