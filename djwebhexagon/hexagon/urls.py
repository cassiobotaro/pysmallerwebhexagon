from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FloatUrlParameterConverter, "float")

urlpatterns = [
    path("<slug:slug>/<float:value>/", views.index, name="index"),
]
