
from django.contrib import admin
from django.urls import path, include


from django.conf import settings  # Nuevo
from django.conf.urls.static import static  # Nuevo


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('empleados.urls'))
]


# Nuevo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)