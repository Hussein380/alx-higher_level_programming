#!/usr/bin/python3

# This script defines a SQLALchemy Base class and a State Class

# importing necessary modules fromSQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a declarative base instance with the custom metadata
Base = declarative_base()


# Defining a class called State, which inherits from the Base class
class State(Base):
    """
    Class with id and name attribute of each state
    """

    # Defining the table name in the database
    __tablename__ = 'states'

    # Defining columns for the 'states'  table
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
