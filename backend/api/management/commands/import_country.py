import csv
from django.core.management.base import BaseCommand
from api.models import Country, Region, CountryRegion

class Command(BaseCommand):
    help = 'Import data from country_region.csv'

    def handle(self, *args, **options):
        csv_file_path = 'data/country_region.csv'

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for row in csv_reader:
                country_name = row[0]
                region_name = row[1]

                # Create or retrieve Country
                country, created = Country.objects.get_or_create(name=country_name)

                # Create or retrieve Region
                region, created = Region.objects.get_or_create(name=region_name)

                # # Create or retrieve CountryRegion
                country_region, created = CountryRegion.objects.get_or_create(country=country, region=region)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))