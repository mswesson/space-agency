from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    """
    Модель слайда

    Хранит в себе:
        название
        изображение
        порядковый номер для сортировки
    """
    title = models.CharField(max_length=200)
    image = FilerImageField(
        related_name="slider_images", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ["order"]  # Сортировка по порядковому номеру

    def __str__(self):
        return self.title
