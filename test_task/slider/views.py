from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Slider


def index(request: HttpRequest) -> HttpResponse:
    """Выводит стартовую страницу"""
    sliders = Slider.objects.all().order_by('order')
    return render(request, 'index.html', {'sliders': sliders})
