from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Slider
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Добавляет приложение Slider в админку"""
    list_display = ("title", "thumbnail")
    fields = ("title", "image")

    def thumbnail(self, obj):
        """Выводит миниатюру изображения в админке"""
        if obj.image:
            #  Создаю кроп версию для админки
            thumbnail_options = {"size": (100, 60), "crop": True}
            thumbnail = get_thumbnailer(obj.image).get_thumbnail(
                thumbnail_options
            )
            html_img_code = (
                f'<img src="{thumbnail.url}" width="100" '
                'height="60" style="object-fit: cover;"/>'
            )
            return format_html(html_img_code)
        return "No Image"

    def get_form(self, request, obj=None, **kwargs):
        """Меняет название в форме создания и изменения слайда"""
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = "Название"
        form.base_fields['image'].label = "Изображение"
        return form

    class Media:
        #  Для перетаскивания в админке
        js = ("adminsortable2/js/adminsortable2.min.js",)

    thumbnail.allow_tags = True
    thumbnail.short_description = "Миниатюра"
