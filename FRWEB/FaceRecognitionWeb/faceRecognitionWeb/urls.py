from django.conf.urls import url
from django.conf.urls import include
from FRW import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('FRW.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
