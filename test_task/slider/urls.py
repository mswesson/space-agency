from django.urls import path

from .views import index, index_2

app_name = "slider"

urlpatterns = [
    path("bootstrap/", index_2, name="index_2"),
    path("css/", index, name="index"),
]
