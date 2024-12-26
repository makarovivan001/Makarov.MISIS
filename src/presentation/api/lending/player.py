from django.urls import path
from lending.views.player import PlayerApiView, PlayerFormApiView


urlpatterns = [
    path('player/', PlayerApiView.as_view({
        'post': 'create',
        'patch': 'change',
        'delete': 'delete',
    })),
    path('player/<int:player_id>/', PlayerApiView.as_view({
        'get': 'get_by_id'
    })),
    path('player/club/<int:club_id>/', PlayerApiView.as_view({
        'get': 'get_by_club_id'
    })),
    path('player/form/', PlayerFormApiView.as_view()),
]
