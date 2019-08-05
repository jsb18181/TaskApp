from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pets import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
