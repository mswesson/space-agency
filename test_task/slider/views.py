from django.shortcuts import render

from .models import Slider


def index(request):
    # Получаем все слайды, отсортированные по полю 'order'
    sliders = Slider.objects.all().order_by('order')

    # Передаём слайды в контекст шаблона
    return render(request, 'index.html', {'sliders': sliders})
