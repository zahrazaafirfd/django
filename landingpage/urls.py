from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landingpage/', include('landingpage.urls')),
]

