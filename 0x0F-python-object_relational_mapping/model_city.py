#!/usr/bin/python3
"""
    This is an ORM Script
    Author: Peter Ekwere
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ This is the State Class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
