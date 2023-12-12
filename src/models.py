import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

    character_favorite = relationship("Character_favorite", back_populates="user")
    planet_favorite = relationship("Planet_favorite", back_populates="user")

    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    diameter = Column(String(50))
    rotation = Column(String(50))
    gravity = Column(String(50))
    climate = Column(String(100))
    terrain = Column(String(100))
    orbital_period = Column(String(100))

    planet_favorite = relationship("Planet_favorite", back_populates="planets")

class Planet_favorite(Base):
    __tablename__ = "planet_favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))

    user = relationship("User", back_populates="planet_favorite")
    planets = relationship("Planets", back_populates="planet_favorite")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    identification = Column(String(100))

    character_favorite = relationship("Character_favorite", back_populates="characters")

class Character_favorite(Base):
    __tablename__ = "character_favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    user = relationship("User", back_populates="character_favorite")
    characters = relationship("Characters", back_populates="character_favorite")







   


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
