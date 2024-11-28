from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "thumbnail")
    fields = ("title", "image")

    def thumbnail(self, obj):
        #  Чтобы в админке были миниатюры изображений
        return f'<img src="{obj.image.url}" width="100" height="60"/>'

    class Media:
        #  Для перетаскивания в админке
        js = ("adminsortable2/js/adminsortable2.min.js",)

    thumbnail.allow_tags = True
