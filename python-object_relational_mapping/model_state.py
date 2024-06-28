#!/usr/bin/python3
"""
Defines a State class and a Base class to map to the 'states' table in the database.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that maps to the 'states' table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
