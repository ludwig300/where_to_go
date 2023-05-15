import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def place_detail_view(request, placeId):
    place = get_object_or_404(Place, placeId=placeId)
    place_data = {
        'title': place.title,
        'imgs': [request.build_absolute_uri(img.photo.url) for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(
        place_data,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )


def index(request):
    places = Place.objects.all()
    places_data = []
    for place in places:
        detailsUrl = reverse('place_detail_view', args=[place.placeId])
        places_data.append({
            'type': 'FeatureCollection',
            'features': [{
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.placeId,
                    'detailsUrl': detailsUrl
                }
            }]})
    context = {'places_data': json.dumps(places_data)}

    return render(request, 'index.html', context)

