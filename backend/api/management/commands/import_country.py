import csv
from django.core.management.base import BaseCommand
from api.models import Country, Region, CountryRegion

class Command(BaseCommand):
    help = 'Import data from country_region.csv'

    def handle(self, *args, **options):
        csv_file_path = 'data/country_region.csv'  # CSVファイルのパスを指定

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # ヘッダー行をスキップする場合

            for row in csv_reader:
                country_name = row[0]  # CSVファイルの該当列に国名があると仮定
                region_name = row[1]  # CSVファイルの該当列に地域名があると仮定

                # Countryを作成または取得
                country, created = Country.objects.get_or_create(name=country_name)

                # Regionを作成または取得
                region, created = Region.objects.get_or_create(name=region_name)

                # CountryRegionを作成
                country_region, created = CountryRegion.objects.get_or_create(country=country, region=region)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))