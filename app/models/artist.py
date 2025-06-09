from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer)
    death_year = Column(Integer)
    nationality = Column(String)

    artworks = relationship("Artwork", back_populates="artist")