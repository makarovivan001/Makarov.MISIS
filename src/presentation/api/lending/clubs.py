from django.urls import path
from lending.views.club import ClubApiView


urlpatterns = [
    path('club/', ClubApiView.as_view({
        'get': 'get_list',
    })),
    path('club/<int:club_id>/', ClubApiView.as_view({
        'get': 'get_by_id',
    })),
]