from django.db.models.fields.files import ImageFieldFile
from pydantic import BaseModel, field_validator, model_validator
from decimal import Decimal

from domain.schemas.lending.club import ClubShortRetrieveDTO
from domain.schemas.lending.country import CountryRetrieveDTO


class PlayerRetrieveDTO(BaseModel):
    id: int
    photo: str
    surname: str
    name: str
    middle_name: str | None
    country_of_birth: CountryRetrieveDTO
    number: int
    club: ClubShortRetrieveDTO
    height: int
    weight: int
    full_games: int
    games: int
    minutes_played: int
    goals: int
    assists: int
    yellow_card: int
    red_card: int
    rating: Decimal

    class Config:
        from_attributes = True

    @field_validator('photo', mode="before")
    @staticmethod
    def image_validator(image: ImageFieldFile | None) -> str:
        if image:
            return image.url
        return ""


class PlayerCreateDTO(BaseModel):
    surname: str
    name: str
    middle_name: str
    number: int
    country_of_birth_id: int
    club_id: int
    height: int = 0
    weight: int = 0
    full_games: int = 0
    games: int = 0
    minutes_played: int = 0
    goals: int = 0
    assists: int = 0
    yellow_card: int = 0
    red_card: int = 0
    rating: Decimal = 0.00


class PlayerUpdateDTO(PlayerCreateDTO):
    id: int


class PlayerDeleteDTO(BaseModel):
    id: int

class PlayerBestRetrieveDTO(BaseModel):
    photo: str
    full_name: str
    number: int
    club: ClubShortRetrieveDTO
    minutes_played: int
    goals: int
    assists: int
    yellow_card: int
    red_card: int
    rating: Decimal

    class Config:
        from_attributes = True

    @field_validator('photo', mode="before")
    @staticmethod
    def image_validator(image: ImageFieldFile | None) -> str:
        if image:
            return image.url
        return ""
