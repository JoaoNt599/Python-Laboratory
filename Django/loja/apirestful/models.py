from django.db import models

from sqlalchemy import Column, Integer, String, Date, Decimal, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    cod_cliente = Column(Integer, primary_key=True)
    nom_cliente = Column(String(100), nullable=False)
    rua_cliente = Column(String(100), nullable=False)
    num_cliente = Column(String(15), nullable=False)

    telefones = relationship("TelefoneCliente", back_populates="cliente")
    emails = relationship("EmailCliente", back_populates="cliente")
    vendas = relationship("Venda", back_populates="cliente")


class TelefoneCliente(Base):
    __tablename__ = 'telefone_cliente'
    cod_cliente = Column(Integer, ForeignKey('cliente.cod_cliente'), primary_key=True)
    tel_cliente = Column(String(11), primary_key=True)

    cliente = relationship("Cliente", back_populates="telefones")


class EmailCliente(Base):
    __tablename__ = 'email_cliente'
    cod_cliente = Column(Integer, ForeignKey('cliente.cod_cliente'), primary_key=True)
    email_cliente = Column(String(15), primary_key=True)

    cliente = relationship("Cliente", back_populates="emails")


class Venda(Base):
    pass
