from pydantic import BaseModel
from typing import Optional

class CultureBase(BaseModel):
    name: str
    region: Optional[str]

class CultureCreate(CultureBase):
    pass

class CultureRead(CultureBase):
    id: int

    class Config:
        from_attributes = True