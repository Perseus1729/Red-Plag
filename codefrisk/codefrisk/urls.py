from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url('backend/',include('backend.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)