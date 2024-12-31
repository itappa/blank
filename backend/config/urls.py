from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        path("", views.index, name="index"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)