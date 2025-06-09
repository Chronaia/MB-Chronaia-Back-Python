from pydantic import BaseModel, HttpUrl
from typing import Optional

class MuseumBase(BaseModel):
    name: str
    slug: str
    location: Optional[str]
    url: Optional[HttpUrl]
    api_source: Optional[str]

class MuseumCreate(MuseumBase):
    pass

class MuseumRead(MuseumBase):
    id: int

    class Config:
        from_attributes = True