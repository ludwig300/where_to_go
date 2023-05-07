from django.db import models


class Place(models.Model):
    placeId = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    detailsUrl = models.URLField(verbose_name='URL подробностей', blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    photo = models.ImageField(
        upload_to='images',
        verbose_name='Изображение',
        null=True
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.id} {self.place.title}'
