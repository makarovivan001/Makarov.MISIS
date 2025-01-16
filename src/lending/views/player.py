from django.db.models import Value
from django.db.models.functions import Concat
from pydantic import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from domain.exceptions.model import ModelDoesNotExistException
from domain.exceptions.validation import ValidationApiException
from domain.schemas.lending.club import ClubShortRetrieveDTO
from domain.schemas.lending.country import CountryRetrieveDTO
from domain.schemas.lending.player import (PlayerRetrieveDTO, PlayerCreateDTO,
                                           PlayerDeleteDTO, PlayerUpdateDTO, PlayerBestRetrieveDTO)
from lending.models import Player, Club, Country


class PlayerApiView(ViewSet):
    def __get_player(self, id) -> dict:
        try:
            player = (
                Player.objects
                .select_related('club', 'country_of_birth')
                .get(id=id)
            )
        except Player.DoesNotExist:
            raise ModelDoesNotExistException

        player_dto = PlayerRetrieveDTO.model_validate(player)
        return player_dto.model_dump()

    def get_by_id(self, request: Request, player_id: int) -> Response:
        return Response(data=self.__get_player(player_id))

    def get_by_club_id(self, request: Request, club_id: int) -> Response:
        players = (
            Player.objects
            .select_related('club', 'country_of_birth')
            .filter(club_id=club_id)
        )
        players = [
            PlayerRetrieveDTO.model_validate(player).model_dump()
            for player in players
        ]
        return Response(data=players)

    def create(self, request: Request) -> Response:
        data = request.data.dict()

        try:
            player_create_dto = PlayerCreateDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        if len(request.FILES) != 0:
            player = Player.objects.create(
                **player_create_dto.model_dump(),
                photo=request.FILES['photo']
            )
        else:
            player = Player.objects.create(**player_create_dto.model_dump())
        return Response(data=self.__get_player(player.pk))

    def change(self, request: Request) -> Response:
        data = request.data.dict()

        try:
            player_update_dto = PlayerUpdateDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        if len(request.FILES) != 0:
            Player.objects.filter(id=player_update_dto.id).update(
                **player_update_dto.model_dump(),
            )
            player = Player.objects.get(id=player_update_dto.id)
            player.photo = request.FILES['photo']
            player.save()
        else:
            Player.objects.filter(id=player_update_dto.id).update(
                **player_update_dto.model_dump(),
            )

        return Response(data=self.__get_player(player_update_dto.id))

    def delete(self, request: Request) -> Response:
        data = request.data

        try:
            player_delete_dto = PlayerDeleteDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        Player.objects.filter(id=player_delete_dto.id).delete()
        return Response({})

    def get_best(self, request: Request) -> Response:
        player_queryset =  Player.objects.all().annotate(
            full_name=Concat('surname', Value(' '), 'name')
        ).select_related('club')
        best_minutes_played = player_queryset.order_by('-minutes_played').first()
        best_goals = player_queryset.order_by('-goals').first()
        best_assists = player_queryset.order_by('-assists').first()
        best_yellow_card = player_queryset.order_by('-yellow_card').first()
        best_red_card = player_queryset.order_by('-red_card').first()
        best_rating = player_queryset.order_by('-rating').first()

        return Response({
            "best_minutes_played": PlayerBestRetrieveDTO.model_validate(best_minutes_played).model_dump(),
            "best_goals": PlayerBestRetrieveDTO.model_validate(best_goals).model_dump(),
            "best_assists": PlayerBestRetrieveDTO.model_validate(best_assists).model_dump(),
            "best_yellow_card": PlayerBestRetrieveDTO.model_validate(best_yellow_card).model_dump(),
            "best_red_card": PlayerBestRetrieveDTO.model_validate(best_red_card).model_dump(),
            "best_rating": PlayerBestRetrieveDTO.model_validate(best_rating).model_dump(),
        })


class PlayerFormApiView(APIView):
    def get(self, request: Request) -> Response:
        club = Club.objects.all()
        country = Country.objects.all()

        data = {
            'clubs': [
                ClubShortRetrieveDTO.model_validate(item).model_dump()
                for item in club
            ],
            'countries': [
                CountryRetrieveDTO.model_validate(item).model_dump()
                for item in country
            ],
        }
        return Response(data=data)