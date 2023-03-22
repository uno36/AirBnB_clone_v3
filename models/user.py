#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes
    User inherits from BaseModel and Base
    class attribute __tablename__
        represents the table name, users
    """
    __tablename__ = "users"
    email = Column(String(128, nullable=False))
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="delete")
    review = relationship("Review", backref="user", cascade="delete")
