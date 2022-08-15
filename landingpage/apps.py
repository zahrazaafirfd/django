from django.contrib import admin
from django.urls import path, include


class LandingpageConfig(AppConfig):
urlpatterns = [
    path('admin/', admin.site.urls),
    path('landingpage/', include('landingpage.urls')),
]
