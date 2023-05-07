import json

from django.shortcuts import render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()
    places_data = []
    for place in places:

        places_data.append({
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.placeId,
                    "detailsUrl": place.detailsUrl
                }
            }]})
    context = {'places_data': json.dumps(places_data)}

    return render(request, 'index.html', context)