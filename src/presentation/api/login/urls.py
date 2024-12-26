from django.urls import path
from login.views import LogoutViewSet, LoginViewSet


urlpatterns = [
    path('login/', LoginViewSet.as_view({
        'post': 'login',
    })),
    path('logout/', LogoutViewSet.as_view({
        'post': 'logout',
    })),
]