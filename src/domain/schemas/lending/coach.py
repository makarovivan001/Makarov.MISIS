from pydantic import BaseModel
from domain.schemas.lending.country import CountryRetrieveDTO


class CoachIDDTO(BaseModel):
    id: int

    class Config:
        from_attributes = True


class CoachNameRetrieveDTO(CoachIDDTO):
    surname: str
    name: str
    middle_name: str | None


class CoachRetrieveDTO(CoachNameRetrieveDTO):
    country: CountryRetrieveDTO


class CoachCreateDTO(BaseModel):
    surname: str
    name: str
    middle_name: str
    country_id: int


class CoachUpdateDTO(CoachCreateDTO):
    id: int


class CoachDeleteDTO(BaseModel):
    id: int
