import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    NameID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld = Column(String(250), ForeignKey('planets.Name'))

class Planets(Base):
    __tablename__ = 'planets'
    PlanetID = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False, unique=True)
    Climate = Column(String(50), nullable=True)
    Residents = Column(Integer, nullable=True)
    rel = relationship(People)

class FavPeople(Base):
    __tablename__ = 'favpeople'
    FavPeopleID = Column(Integer, primary_key=True)
    people = Column(String(250), ForeignKey('people.name'))
    user_ID = Column(String(250), ForeignKey('users.Email'))

class FavPlanets(Base):
    __tablename__ = 'favplanet'
    FavPlanetID = Column(Integer, primary_key=True)
    planets = Column(String(250), ForeignKey('planets.name'))
    user_ID = Column(String(250), ForeignKey('users.Email'))

class Users(Base):
    __tablename__ = 'users'
    UserID = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False, unique=True)
    Email = Column(String(100), nullable=False, unique=True)
    Password = Column(String(50), nullable=False, unique=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')