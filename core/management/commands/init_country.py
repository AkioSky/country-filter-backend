from django.core.management.base import BaseCommand
import json

from ...models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('countries.json') as json_file:
            data = json.load(json_file)

            # Print the data of dictionary
            countries = []
            [countries.append(Country(name=country['name'])) for country in data]
            Country.objects.bulk_create(countries)

