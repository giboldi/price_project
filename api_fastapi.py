from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_engine, Base, Producto, Categoria, Usuario, Venta, sessionmaker
from pydantic import BaseModel
from typing import List

# Inicializar FastAPI
app = FastAPI()

# Configurar la sesión de base de datos
engine = get_engine()
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Esquemas de Pydantic
class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    categoria_id: int
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    class Config:
        from_attributes = True

# Rutas para CRUD de Productos
@app.post("/productos/", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@app.get("/productos/", response_model=List[ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()

@app.get("/productos/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.put("/productos/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, producto: ProductoCreate, db: Session = Depends(get_db)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for key, value in producto.model_dump().items():
        setattr(db_producto, key, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(db_producto)
    db.commit()
    return {"mensaje": "Producto eliminado"}
