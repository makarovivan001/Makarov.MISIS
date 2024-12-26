from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from football_analytics import settings
from presentation.urls import urlpatterns as routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers)),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^staticfiles/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
