from django.urls import path, include
from .lending.clubs import urlpatterns as clubs_urls
from .lending.player import urlpatterns as players_urls
from .lending.coach import urlpatterns as coaches_urls
from .login.urls import urlpatterns as login_urls


urlpatterns = [
    path('v1/', include(login_urls)),
    path('v1/', include(clubs_urls)),
    path('v1/', include(players_urls)),
    path('v1/', include(coaches_urls)),
]