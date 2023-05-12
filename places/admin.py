from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']
    fields = ['photo', 'image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;">', obj.photo.url)
    image_preview.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
