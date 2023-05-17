import os
import requests
import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files.base import ContentFile

from places.models import Place, Image


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
                'description_short': place_info['description_short'],
                'description_long': place_info['description_long'],
                'lng': float(place_info['coordinates']['lng']),
                'lat': float(place_info['coordinates']['lat']),
            },
        )

        if created:
            for img_url in place_info['imgs']:
                image_filename = os.path.basename(img_url)
                image_path = os.path.join(settings.MEDIA_ROOT, image_filename)
                response = requests.get(img_url)
                response.raise_for_status()

                image_content = ContentFile(response.content)
                image = Image.objects.create(place=place)
                image.photo.save(image_filename, image_content, save=True)

            place.save()

            self.stdout.write(
                self.style.SUCCESS(f'Successfully loaded place: {place.title}')
            )
