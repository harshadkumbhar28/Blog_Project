from django.contrib import admin
from django.urls import path, include
from .views import base, index
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="home"),
                  path('base/', base, name="base")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
