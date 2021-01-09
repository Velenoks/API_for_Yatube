from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from yatube_api import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='posts-api')),
    path('redoc/',
         TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
