from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Period(Base):
    __tablename__ = "periods"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_year = Column(Integer)
    end_year = Column(Integer)

    artworks = relationship("Artwork", back_populates="period")