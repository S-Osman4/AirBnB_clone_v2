#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel):
    """ The city class, contains state ID and name
    Attributes:
        name: input name
        state_id: input state id
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref='cities', cascade="delete")
