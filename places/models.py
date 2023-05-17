from django.db import models
from ckeditor.fields import RichTextField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = RichTextField(blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Image(models.Model):
    photo = models.ImageField(
        upload_to='images',
        verbose_name='Изображение'
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.id} {self.place.title}'
