from sqlalchemy.orm import joinedload
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Producto

router = APIRouter()

# Optimización de consulta: Uso de joinedload para reducir el número de queries
@router.get("/productos/")
def listar_productos(db: Session = Depends(get_db)):
    productos = db.query(Producto).options(joinedload(Producto.categoria)).all()
    return productos

# Optimización de búsqueda en Typesense usando filtros eficientes
@router.get("/search/")
def buscar_productos(query: str, categoria_id: int = None):
    search_params = {
        "q": query,
        "query_by": "nombre,descripcion",
        "filter_by": f"categoria_id:={categoria_id}" if categoria_id else ""
    }
    
    from typesense_integration import client
    results = client.collections["productos"].documents.search(search_params)
    return results["hits"]
