from pydantic import BaseModel


class CountryRetrieveDTO(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True