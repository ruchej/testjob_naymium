from django.urls import include, path


urlpatterns = [
    path("", include("main.api.v1.urls")),
    path("v1/", include("main.api.v1.urls")),
]
