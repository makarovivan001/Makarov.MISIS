from django.db.models.fields.files import ImageFieldFile
from pydantic import BaseModel, field_validator
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


class PlayerUpdateDTO(PlayerCreateDTO):
    id: int


class PlayerDeleteDTO(BaseModel):
    id: int