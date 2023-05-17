import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    

    

class Personas(Base):
    __tablename__ = 'personas' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), unique=True, nullable=False)
    genero = Column(String(10), nullable=False)
    year_nacimiento = Column(String(10), nullable=False)
    color_de_ojos = Column(String(20), nullable=False)
    color_de_piel = Column(String(20), nullable=False)
    color_de_pelo = Column(String(20), nullable=False)
    Peso = Column(Integer, nullable=False)
    altura = Column(Integer, nullable=False)
    favoritos_personas_id = Column(Integer, ForeignKey('favoritos_personas.id'))


class Planetas(Base):
    __tablename__ = 'planetas' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), unique=True, nullable=False)
    diametro = Column(Integer, nullable=False)
    periodo_rotacion = Column(Integer, nullable=False)
    periodo_orbital = Column(Integer, nullable=False)
    gravedad = Column(String(60), nullable=False)
    poblacion = Column(Integer, nullable=False)
    clima = Column(String(80), nullable=False)
    terreno = Column(String(100), nullable=False)
    superficie_liquida = Column(Integer, nullable=False)
    favoritos_planetas_id = Column(Integer, ForeignKey('favoritos_planetas.id'))


class Vehiculos(Base):
    __tablename__ = 'vehiculos' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), unique=True, nullable=False)
    modelo = Column(String(120), nullable=False)
    clase = Column(String(120), nullable=False)
    constructor = Column(String(120), nullable=False)
    coste = Column(Integer, nullable=False)
    longitud = Column(Integer, nullable=False)
    tripulacion = Column(Integer, nullable=False)
    pasajeros = Column(Integer, nullable=False)
    velocidad_maxima = Column(Integer, nullable=False)
    capacidad_carga = Column(Integer, nullable=False)
    provisiones = Column(String(100), nullable=False)
    favoritos_vehiculos_id = Column(Integer, ForeignKey('favoritos_vehiculos.id'))
    

class Favoritos_personas(Base):
    __tablename__ = 'favoritos_personas' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    personas_id = Column(Integer, nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

class Favoritos_planetas(Base):
    __tablename__ = 'favoritos_planetas' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    planetas_id = Column(Integer, nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

class Favoritos_vehiculos(Base):
    __tablename__ = 'favoritos_vehiculos' 
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    vehiculos_id = Column(Integer, nullable=True)
    # vehiculos = relationship('Vehiculos', backref='favoritos_vehiculos', lazy=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
