from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from domain.exceptions.model import ModelDoesNotExistException
from domain.exceptions.validation import ValidationApiException
from domain.schemas.lending.coach import (CoachRetrieveDTO, CoachCreateDTO,
                                          CoachUpdateDTO, CoachDeleteDTO)
from domain.schemas.lending.country import CountryRetrieveDTO
from lending.models import Country, Coach


class CoachApiView(ViewSet):
    def __get_coach(self, id: int) -> dict:
        try:
            coach = (
                Coach.objects
                .select_related('country')
                .get(id=id)
            )
        except Coach.DoesNotExist:
            raise ModelDoesNotExistException

        coach_dto = CoachRetrieveDTO.model_validate(coach)
        return coach_dto.model_dump()

    def get_by_id(self, request: Request, coach_id: int) -> Response:
        return Response(data=self.__get_coach(coach_id))

    def create(self, request: Request) -> Response:
        data = request.data

        try:
            coach_create_dto = CoachCreateDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        coach = Coach.objects.create(**coach_create_dto.model_dump())
        return Response(data=self.__get_coach(coach.pk))

    def change(self, request: Request) -> Response:
        data = request.data

        try:
            coach_update_dto = CoachUpdateDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        Coach.objects.filter(id=coach_update_dto.id).update(
            **coach_update_dto.model_dump()
        )
        return Response(data=self.__get_coach(coach_update_dto.id))

    def delete(self, request: Request) -> Response:
        data = request.data

        try:
            coach_delete_dto = CoachDeleteDTO(**data)
        except ValidationError as exc:
            raise ValidationApiException(exc.errors())

        Coach.objects.filter(id=coach_delete_dto.id).delete()
        return Response({})


class CoachFormApiView(APIView):
    def get(self, request: Request) -> Response:
        country = Country.objects.all()

        data = {
            'countries': [
                CountryRetrieveDTO.model_validate(item).model_dump()
                for item in country
            ],
        }
        return Response(data=data)