from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Country, Region, Year, CountryRegion

class ViewsTestCase(APITestCase):
    def setUp(self):
        # テスト用ユーザーの作成
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # テストデータの作成
        self.country = Country.objects.create(name='Test Country')
        self.region = Region.objects.create(name='Test Region')
        self.year = Year.objects.create(year=2021)
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)

    def test_get_routes(self):
        response = self.client.get('/api/test/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_view_set(self):
        self.client.force_authenticate(user=self.user)  # 認証されたユーザーでテスト
        response = self.client.get(reverse('country-list'))  # URL名を使用してリバースルックアップ
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_region_view_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('region-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_year_view_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('year-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_region_view_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('countryregion-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_economic_data_view_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('economicdata-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_social_support_data_view_set(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('socialsupportdata-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
