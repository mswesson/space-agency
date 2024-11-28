from django.urls import path

from .views import index

app_name = "slider"

urlpatterns = [
    path("", index, name="index"),
]
