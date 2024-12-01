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

    title = models.CharField(max_length=200, verbose_name="Название")
    image = FilerImageField(
        related_name="slider_images",
        on_delete=models.CASCADE,
        verbose_name="Изображение",
    )
    order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name="Порядок"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return self.title
