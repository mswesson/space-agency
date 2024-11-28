from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "thumbnail")
    fields = ("title", "image")

    def thumbnail(self, obj):
        return f'<img src="{obj.image.url}" width="100" height="60"/>'

    class Media:
        js = ("adminsortable2/js/adminsortable2.min.js",)

    thumbnail.allow_tags = True
