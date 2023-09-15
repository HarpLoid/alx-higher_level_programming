#!/usr/bin/python3
"""
Defines class City
"""

from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """
    City class
    Atrrib: id, name, state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
