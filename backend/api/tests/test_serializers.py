from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from api.serializers import (
    RegisterSerializer, CountrySerializer, RegionSerializer, YearSerializer,
    CountryRegionSerializer, EconomicDataSerializer
)
from api.models import Country, Region, Year, CountryRegion, EconomicData

class SerializersTestCase(TestCase):
    def setUp(self):
        # 必要なテストデータをセットアップ
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.region = Region.objects.create(name='Test Region')
        self.country = Country.objects.create(name='Test Country')
        self.country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        self.year = Year.objects.create(year=2021)

    def test_register_serializer(self):
        data = {'username': 'newuser', 'password': 'newpassword', 'password2': 'newpassword'}
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'newuser')

    def test_country_serializer(self):
        data = {'name': 'New Country', 'region_id': self.region.pk}
        serializer = CountrySerializer(data=data)
        self.assertTrue(serializer.is_valid())
        country = serializer.save()
        self.assertEqual(country.name, 'New Country')
        self.assertEqual(country.regions.first(), self.region)

    def test_region_serializer(self):
        serializer = RegionSerializer(self.region)
        self.assertEqual(serializer.data, {'id': self.region.pk, 'name': 'Test Region'})

    def test_year_serializer(self):
        serializer = YearSerializer(self.year)
        self.assertEqual(serializer.data, {'id': self.year.pk, 'year': 2021})

    def test_country_region_serializer(self):
        data = {'country_id': self.country.pk, 'region_id': self.region.pk}
        serializer = CountryRegionSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        country_region = serializer.save()
        self.assertEqual(country_region.country, self.country)
        self.assertEqual(country_region.region, self.region)

    def test_economic_data_serializer(self):
        data = {
            'country_region_id': self.country_region.pk,
            'year_id': self.year.pk,
            'gdp': '12345.678'
        }
        serializer = EconomicDataSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        economic_data = serializer.save()
        self.assertEqual(economic_data.gdp, '12345.678')
