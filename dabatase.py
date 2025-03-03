from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"))
    precio = Column(DECIMAL(10,2), nullable=False)
    stock = Column(Integer, nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey("productos.id", ondelete="CASCADE"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    cantidad = Column(Integer, nullable=False)
    fecha = Column(TIMESTAMP, server_default=func.current_timestamp())
