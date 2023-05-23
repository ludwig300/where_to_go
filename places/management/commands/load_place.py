import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = 'Load places data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='URL of the JSON file')

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        response.raise_for_status()
        place_info = response.json()

        place, created = Place.objects.get_or_create(
            title=place_info['title'],
            defaults={
                'description_short': place_info.get('description_short', ''),
                'description_long': place_info.get('description_long', ''),
                'lng': place_info['coordinates']['lng'],
                'lat': place_info['coordinates']['lat'],
            },
        )

        if not created:
            return

        for img_url in place_info.get('imgs', []):
            image_filename = os.path.basename(img_url)
            response = requests.get(img_url)
            response.raise_for_status()

            image_content = ContentFile(response.content)
            place.image_set.create(photo=image_content, name=image_filename)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded place: {place.title}')
        )
