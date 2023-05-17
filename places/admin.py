from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']
    fields = ['photo', 'image_preview']

    def image_preview(self, image):
        return format_html('<img src="{}" style="max-height: 200px;">', image.photo.url)
    image_preview.short_description = 'Preview'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
