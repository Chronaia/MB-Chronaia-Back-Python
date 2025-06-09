from pydantic import BaseModel, HttpUrl
from typing import Optional

from .museum import MuseumRead
from .artist import ArtistRead
from .department import DepartmentRead
from .culture import CultureRead
from .period import PeriodRead
from .category import CategoryRead

class ArtworkBase(BaseModel):
    title: str
    image_url: Optional[HttpUrl]
    medium: Optional[str]
    object_url: Optional[HttpUrl]
    object_date: Optional[str]

class ArtworkCreate(ArtworkBase):
    museum_id: int
    artist_id: Optional[int]
    department_id: Optional[int]
    culture_id: Optional[int]
    period_id: Optional[int]
    category_id: Optional[int]

class ArtworkRead(ArtworkBase):
    id: int
    museum: MuseumRead
    artist: Optional[ArtistRead]
    department: Optional[DepartmentRead]
    culture: Optional[CultureRead]
    period: Optional[PeriodRead]
    category: Optional[CategoryRead]

    class Config:
        from_attributes = True