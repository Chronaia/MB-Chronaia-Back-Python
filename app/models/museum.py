from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Museum(Base):
    __tablename__ = "museums"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    location = Column(String)
    url = Column(String)
    api_source = Column(String)

    artworks = relationship("Artwork", back_populates="museum")