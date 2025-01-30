from django.contrib import admin
from django.urls import path, include
from app.custom_admin import second_admin_site
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('second_admin/', second_admin_site.urls),
    path('', include('app.urls')),
    path('api/', include("api.urls")),
    path('api-rest/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

