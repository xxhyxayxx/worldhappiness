from django.test import TestCase
from api.models import Country, Region, CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, GenerosityData, GovernmentTrustData, HappinessScore

class CountryModelTestCase(TestCase):
    def test_create_country(self):
        # 新しい国を作成してデータベースに保存
        country = Country.objects.create(name="Test Country")
        
        # データベースに保存されているか確認
        self.assertEqual(Country.objects.count(), 1)
        
        # 作成した国の名前を取得して確認
        self.assertEqual(country.name, "Test Country")

    def test_country_str(self):
        # 国の文字列表現が正しいか確認
        country = Country.objects.create(name="Test Country")
        self.assertEqual(str(country), "Test Country")

    def test_add_region_to_country(self):
        # 国に関連する地域情報を追加できるか確認
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")
        
        country.regions.add(region)
        
        self.assertEqual(country.regions.count(), 1)


class RegionModelTestCase(TestCase):
    def test_create_region(self):
        # 新しい地域を作成してデータベースに保存
        region = Region.objects.create(name="Test Region")
        
        # データベースに保存されているか確認
        self.assertEqual(Region.objects.count(), 1)
        
        # 作成した地域の名前を取得して確認
        self.assertEqual(region.name, "Test Region")

    def test_region_str(self):
        # 地域の文字列表現が正しいか確認
        region = Region.objects.create(name="Test Region")
        self.assertEqual(str(region), "Test Region")


class CountryRegionModelTestCase(TestCase):
    def setUp(self):
        # テストに使用する Country と Region のインスタンスを作成
        self.country = Country.objects.create(name="Test Country")
        self.region = Region.objects.create(name="Test Region")

    def test_create_country_region(self):
        # 新しい CountryRegion を作成してデータベースに保存
        country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        
        # データベースに保存されているか確認
        self.assertEqual(CountryRegion.objects.count(), 1)
        
        # 作成した CountryRegion の関連が正しいか確認
        self.assertEqual(country_region.country, self.country)
        self.assertEqual(country_region.region, self.region)

    def test_cascade_deletion(self):
        # CountryRegion を作成
        country_region = CountryRegion.objects.create(country=self.country, region=self.region)
        
        # Country を削除
        self.country.delete()
        
        # CountryRegion も削除されたか確認
        self.assertEqual(CountryRegion.objects.count(), 0)

class CommonFieldsModelTestCase(TestCase):
    def test_create_economic_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # EconomicDataモデルを作成
        economic_data = EconomicData.objects.create(
            country_region=country_region,
            year=year,
            gdp=12345.678  # ここに適切な値を設定
        )

        # 作成したEconomicDataがデータベースに保存されているか確認
        self.assertEqual(EconomicData.objects.count(), 1)

        # 作成したEconomicDataの関連が正しいか確認
        self.assertEqual(economic_data.country_region, country_region)
        self.assertEqual(economic_data.year, year)
        self.assertEqual(economic_data.gdp, 12345.678) 

    def test_create_social_support_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # SocialSupportDataモデルを作成
        social_support_data = SocialSupportData.objects.create(
            country_region=country_region,
            year=year,
            social_support=0.789  # ここに適切な値を設定
        )

        # 作成したSocialSupportDataがデータベースに保存されているか確認
        self.assertEqual(SocialSupportData.objects.count(), 1)

        # 作成したSocialSupportDataの関連が正しいか確認
        self.assertEqual(social_support_data.country_region, country_region)
        self.assertEqual(social_support_data.year, year)
        self.assertEqual(social_support_data.social_support, 0.789)

    def test_create_health_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # HealthDataモデルを作成
        health_data = HealthData.objects.create(
            country_region=country_region,
            year=year,
            life_expectancy=75.6  # ここに適切な値を設定
        )

        # 作成したHealthDataがデータベースに保存されているか確認
        self.assertEqual(HealthData.objects.count(), 1)

        # 作成したHealthDataの関連が正しいか確認
        self.assertEqual(health_data.country_region, country_region)
        self.assertEqual(health_data.year, year)
        self.assertEqual(health_data.life_expectancy, 75.6)

    def test_create_freedom_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # FreedomDataモデルを作成
        freedom_data = FreedomData.objects.create(
            country_region=country_region,
            year=year,
            freedom=0.654  # ここに適切な値を設定
        )

        # 作成したFreedomDataがデータベースに保存されているか確認
        self.assertEqual(FreedomData.objects.count(), 1)

        # 作成したFreedomDataの関連が正しいか確認
        self.assertEqual(freedom_data.country_region, country_region)
        self.assertEqual(freedom_data.year, year)
        self.assertEqual(freedom_data.freedom, 0.654)

    def test_create_generosity_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # GenerosityDataモデルを作成
        generosity_data = GenerosityData.objects.create(
            country_region=country_region,
            year=year,
            generosity=0.567  # ここに適切な値を設定
        )

        # 作成したGenerosityDataがデータベースに保存されているか確認
        self.assertEqual(GenerosityData.objects.count(), 1)

        # 作成したGenerosityDataの関連が正しいか確認
        self.assertEqual(generosity_data.country_region, country_region)
        self.assertEqual(generosity_data.year, year)
        self.assertEqual(generosity_data.generosity, 0.567)

    def test_create_government_trust_data(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # GovernmentTrustDataモデルを作成
        government_trust_data = GovernmentTrustData.objects.create(
            country_region=country_region,
            year=year,
            government_trust=0.678  # ここに適切な値を設定
        )

        # 作成したGovernmentTrustDataがデータベースに保存されているか確認
        self.assertEqual(GovernmentTrustData.objects.count(), 1)

        # 作成したGovernmentTrustDataの関連が正しいか確認
        self.assertEqual(government_trust_data.country_region, country_region)
        self.assertEqual(government_trust_data.year, year)
        self.assertEqual(government_trust_data.government_trust, 0.678)

    def test_create_happiness_score(self):
        # CountryとRegionを作成
        country = Country.objects.create(name="Test Country")
        region = Region.objects.create(name="Test Region")

        # CountryRegionとYearを作成
        country_region = CountryRegion.objects.create(country=country, region=region)
        year = Year.objects.create(year=2023)

        # HappinessScoreモデルを作成
        happiness_score_data = HappinessScore.objects.create(
            country_region=country_region,
            year=year,
            happiness_score=7.89  # ここに適切な値を設定
        )

        # 作成したHappinessScoreがデータベースに保存されているか確認
        self.assertEqual(HappinessScore.objects.count(), 1)

        # 作成したHappinessScoreの関連が正しいか確認
        self.assertEqual(happiness_score_data.country_region, country_region)
        self.assertEqual(happiness_score_data.year, year)
        self.assertEqual(happiness_score_data.happiness_score, 7.89)

