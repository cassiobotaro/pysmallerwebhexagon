from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hexagon/", include("hexagon.urls")),
    path("admin/", admin.site.urls),
]
