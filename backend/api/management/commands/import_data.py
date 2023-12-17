import csv
import re
import os
from django.core.management.base import BaseCommand
from api.models import CountryRegion, Year, EconomicData, SocialSupportData, HealthData, FreedomData, GenerosityData, GovernmentTrustData, HappinessScore

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **options):
        csv_directory = 'data/'

        # Iterate through CSV files (to handle multiple files)
        for filename in os.listdir(csv_directory):
            if filename.endswith(".csv"):
                csv_file_path = os.path.join(csv_directory, filename)

                # Extract year from file name
                match = re.search(r'_(\d{4})\.csv', filename)
                if match:
                    year_value = int(match.group(1))
                else:
                    self.stdout.write(self.style.ERROR(f"Could not extract year from file name: {filename}"))
                    continue

                if year_value is not None:
                    with open(csv_file_path, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)

                        for row in csv_reader:
                            country_name = row[0] 

                            # Find the corresponding CountryRegion
                            try:
                                country_region = CountryRegion.objects.get(country__name=country_name)
                            except CountryRegion.DoesNotExist:
                                self.stdout.write(self.style.ERROR(f"CountryRegion for {country_name} not found."))
                                continue

                            # Create or retrieve Year models
                            year, created = Year.objects.get_or_create(year=year_value)

                            # Insert data for each year into the appropriate model
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