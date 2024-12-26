from django.urls import path, include
from .api.urls import urlpatterns as api_patterns
from .templates.urls import urlpatterns as templates_patterns


urlpatterns = [
    path('', include(templates_patterns)),
    path('api/', include(api_patterns)),
]