import csv
import re
import os
from django.core.management.base import BaseCommand
from api.models import CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, GenerosityData, GovernmentTrustData, HappinessScore

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **options):
        # CSVファイルが保存されているディレクトリのパスを指定
        csv_directory = 'data/'  # 例: 'data/csv_files/'

        # CSVファイルを反復処理
        for filename in os.listdir(csv_directory):
            if filename.endswith(".csv"):
                csv_file_path = os.path.join(csv_directory, filename)

                # 正規表現を使用してファイル名から年を抽出
                match = re.search(r'_(\d{4})\.csv', filename)
                if match:
                    year_value = int(match.group(1))
                else:
                    self.stdout.write(self.style.ERROR(f"Could not extract year from file name: {filename}"))
                    continue

                if year_value is not None:
                    # CSVファイルを開いてデータを読み込む
                    with open(csv_file_path, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # ヘッダー行をスキップする場合

                        for row in csv_reader:
                            # CSVファイルからデータを読み込む
                            country_name = row[0]  # CSVファイルの該当列に国名があると仮定

                            # 対応するCountryRegionを見つける
                            try:
                                country_region = CountryRegion.objects.get(country__name=country_name)
                            except CountryRegion.DoesNotExist:
                                self.stdout.write(self.style.ERROR(f"CountryRegion for {country_name} not found."))
                                continue

                            # Yearモデルを作成または取得
                            year, created = Year.objects.get_or_create(year=year_value)

                            # 各年のデータを適切なモデルに挿入
                            EconomicData.objects.create(country_region=country_region, year=year, gdp=row[2])
                            SocialSupportData.objects.create(country_region=country_region, year=year, social_support=row[3])
                            HealthData.objects.create(country_region=country_region, year=year, life_expectancy=row[4])
                            FreedomData.objects.create(country_region=country_region, year=year, freedom=row[5])
                            GenerosityData.objects.create(country_region=country_region, year=year, generosity=row[6])
                            GovernmentTrustData.objects.create(country_region=country_region, year=year, government_trust=row[7])
                            HappinessScore.objects.create(country_region=country_region, year=year, happiness_score=row[1])

                    self.stdout.write(self.style.SUCCESS(f"Data insertion completed for year: {year_value}"))
                else:
                    self.stdout.write(self.style.ERROR("Year value not found."))