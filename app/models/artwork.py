from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Artwork(Base):
    __tablename__ = "artworks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    image_url = Column(String)
    medium = Column(String)
    object_url = Column(String)
    object_date = Column(String)

    museum_id = Column(Integer, ForeignKey("museums.id"))
    artist_id = Column(Integer, ForeignKey("artists.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    culture_id = Column(Integer, ForeignKey("cultures.id"))
    period_id = Column(Integer, ForeignKey("periods.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    museum = relationship("Museum", back_populates="artworks")
    artist = relationship("Artist", back_populates="artworks")
    department = relationship("Department", back_populates="artworks")
    culture = relationship("Culture", back_populates="artworks")
    period = relationship("Period", back_populates="artworks")
    category = relationship("Category", back_populates="artworks")