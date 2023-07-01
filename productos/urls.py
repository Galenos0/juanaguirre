from django.urls import path
from . import views


urlpatterns = [
    path("agregar/", views.add_product, name="agregar_producto"),
    path("", views.show_product, name="base")
]