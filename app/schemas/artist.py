from pydantic import BaseModel
from typing import Optional

class ArtistBase(BaseModel):
    name: str
    birth_year: Optional[int]
    death_year: Optional[int]
    nationality: Optional[str]

class ArtistCreate(ArtistBase):
    pass

class ArtistRead(ArtistBase):
    id: int

    class Config:
        from_attributes = True