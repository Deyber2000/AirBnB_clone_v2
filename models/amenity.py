#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import Place


class Amenity(BaseModel, Base):
    """Define class Amanity and map to amenities table in a DB"""
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=Place.place_amenity,
            viewonly=False)
    else:
        name = ""
