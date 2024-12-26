from django.db.models.fields.files import ImageFieldFile
from pydantic import BaseModel, field_validator

from domain.schemas.lending.coach import CoachNameRetrieveDTO
from domain.schemas.lending.country import CountryRetrieveDTO


class PlayerClubInfoRetrieveDTO(BaseModel):
    id: int
    photo: str
    surname: str
    name: str
    middle_name: str | None
    country_of_birth: CountryRetrieveDTO
    number: int

    class Config:
        from_attributes = True

    @field_validator('photo', mode="before")
    @staticmethod
    def image_validator(image: ImageFieldFile | None) -> str:
        if image:
            return image.url
        return ""


class ClubShortRetrieveDTO(BaseModel):
    id: int
    name: str
    photo: str

    class Config:
        from_attributes = True

    @field_validator('photo', mode="before")
    @staticmethod
    def image_validator(image: ImageFieldFile | None) -> str:
        if image:
            return image.url
        return ""


class ClubRetrieveDTO(ClubShortRetrieveDTO):
    id: int
    name: str
    description: str
    country: CountryRetrieveDTO
    coach: CoachNameRetrieveDTO
    player: list[PlayerClubInfoRetrieveDTO]

    @field_validator('player', mode='before')
    @staticmethod
    def player_validator(value):
        return value.all()


class ClubListRetrieveDTO(BaseModel):
    clubs: list[ClubRetrieveDTO]

    class Config:
        from_attributes = True
