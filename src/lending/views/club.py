from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from domain.exceptions.model import ModelDoesNotExistException
from domain.schemas.lending.club import ClubRetrieveDTO, ClubShortRetrieveDTO
from lending.models import Club


class ClubApiView(ViewSet):
    def get_list(self, request: Request) -> Response:
        clubs = Club.objects.select_related(
            'coach',
            'country'
        ).all()
        clubs_dto = [
            ClubShortRetrieveDTO.model_validate(club).model_dump()
            for club in clubs
        ]

        data = {
            'clubs': clubs_dto
        }
        return Response(data=data)

    def get_by_id(self, request: Request, club_id: int) -> Response:
        try:
            club = Club.objects.prefetch_related('player', 'player__country_of_birth').get(id=club_id)
        except Club.DoesNotExist:
            raise ModelDoesNotExistException

        return Response(data=ClubRetrieveDTO.model_validate(club).model_dump())