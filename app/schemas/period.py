from pydantic import BaseModel
from typing import Optional

class PeriodBase(BaseModel):
    name: str
    start_year: Optional[int]
    end_year: Optional[int]

class PeriodCreate(PeriodBase):
    pass

class PeriodRead(PeriodBase):
    id: int

    class Config:
        from_attributes = True