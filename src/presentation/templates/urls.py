from django.urls import path
from lending.views.template_views import index


urlpatterns = [
    path('', index)
]