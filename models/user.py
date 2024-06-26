#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
