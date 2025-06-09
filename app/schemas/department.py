from pydantic import BaseModel

class DepartmentBase(BaseModel):
    name: str
    slug: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentRead(DepartmentBase):
    id: int

    class Config:
        from_attributes = True