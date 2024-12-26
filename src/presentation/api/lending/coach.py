from django.urls import path
from lending.views.coach import CoachApiView, CoachFormApiView


urlpatterns = [
    path('coach/', CoachApiView.as_view({
        'post': 'create',
        'patch': 'change',
        'delete': 'delete'
    })),
    path('coach/<int:coach_id>/', CoachApiView.as_view({
        'get': 'get_by_id'
    })),
    path('coach/form/', CoachFormApiView.as_view()),
]