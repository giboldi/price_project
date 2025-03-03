import pytest
from fastapi.testclient import TestClient
from api_fastapi import app
from database import get_engine, Base, Producto, sessionmaker
from sqlalchemy.orm import Session

# Configuración de la base de datos de pruebas
engine = get_engine()
TestingSessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Pruebas

def test_crear_producto():
    response = client.post("/productos/", json={
        "nombre": "Producto Test",
        "descripcion": "Descripción de prueba",
        "categoria_id": 1,
        "precio": 10.99,
        "stock": 100
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Producto Test"

def test_listar_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obtener_producto():
    response = client.get("/productos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_actualizar_producto():
    response = client.put("/productos/1", json={
        "nombre": "Producto Modificado",
        "descripcion": "Nueva descripción",
        "categoria_id": 1,
        "precio": 15.99,
        "stock": 50
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Producto Modificado"

def test_eliminar_producto():
    response = client.delete("/productos/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto eliminado"
