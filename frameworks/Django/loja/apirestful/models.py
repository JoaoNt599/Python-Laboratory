from django.db import models

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.types import DECIMAL


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
    __tablename__ = 'venda'
    num_pedido = Column(Integer, primary_key=True)
    dta_pedido = Column(Date, nullable=False)
    cod_cliente = Column(Integer, ForeignKey('cliente.cod_cliente'), nullable=False)

    cliente = relationship("Cliente", back_populates="vendas")
    produtos = relationship("VendaContemProduto", back_populates="venda")


class Produto(Base):
    __tablename__ = 'produto'
    cod_produto = Column(Integer, primary_key=True)
    nom_produto = Column(String(100), nullable=False)
    est_produto = Column(Integer, default=0)
    pco_produto = Column(DECIMAL(10, 2), default=0)
    fabricante = Column(String(100), nullable=False)


class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    cod_fornecedor = Column(Integer, primary_key=True)
    nom_fornecedor = Column(String(100), nullable=False)
    rua_fornecedor = Column(String(100), nullable=False)
    num_fornecedor = Column(String(15), nullable=False)

    telefones = relationship("TelefoneFornecedor", back_populates="fornecedor")
    emails = relationship("EmailFornecedor", back_populates="fornecedor")
    compras = relationship("Compra", back_populates="fornecedor")


class TelefoneFornecedor(Base):
    __tablename__ = 'telefone_fornecedor'
    cod_fornecedor = Column(Integer, ForeignKey('fornecedor.cod_fornecedor'), primary_key=True)
    tel_fornecedor = Column(String(11), primary_key=True)
    
    fornecedor = relationship("Fornecedor", back_populates="telefones")


class EmailFornecedor(Base):
    __tablename__ = 'email_fornecedor'
    cod_fornecedor = Column(Integer, ForeignKey('fornecedor.cod_fornecedor'), primary_key=True)
    email_fornecedor = Column(String(15), primary_key=True)
    
    fornecedor = relationship("Fornecedor", back_populates="emails")


class Compra(Base):
    __tablename__ = 'compra'
    num_pedido = Column(Integer, primary_key=True)
    dta_pedido = Column(Date, nullable=False)
    cod_fornecedor = Column(Integer, ForeignKey('fornecedor.cod_fornecedor'), nullable=False)
    
    fornecedor = relationship("Fornecedor", back_populates="compras")
    produtos = relationship("PedidoEstaCompra", back_populates="compra")


class PedidoEstaCompra(Base):
    __tablename__ = 'pedido_esta_compra'
    num_pedido = Column(Integer, ForeignKey('compra.num_pedido'), primary_key=True)
    cod_produto = Column(Integer, ForeignKey('produto.cod_produto'), primary_key=True)
    
    compra = relationship("Compra", back_populates="produtos")
    produto = relationship("Produto")


class VendaContemProduto(Base):
    __tablename__ = 'venda_contem_produto'
    num_pedido = Column(Integer, ForeignKey('venda.num_pedido'), primary_key=True)
    cod_produto = Column(Integer, ForeignKey('produto.cod_produto'), primary_key=True)
    pco_produto = Column(DECIMAL(10, 2), default=0)
    qtd_produto = Column(Integer, default=0)
    
    venda = relationship("Venda", back_populates="produtos")
    produto = relationship("Produto")
    