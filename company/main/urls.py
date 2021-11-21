from django.urls import include, path


urlpatterns = [
    path("", include("main.api.urls")),
]
