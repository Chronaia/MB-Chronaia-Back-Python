from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Culture(Base):
    __tablename__ = "cultures"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String)

    artworks = relationship("Artwork", back_populates="culture")