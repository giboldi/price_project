import typesense
from sqlalchemy.orm import Session
from database import get_engine, Producto, sessionmaker

# Configurar el cliente de Typesense
client = typesense.Client({
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'api_key': 'xyz',  # Cambiar por la clave correcta
    'connection_timeout_seconds': 2
})

# Definir el esquema en Typesense
schema = {
    'name': 'productos',
    'fields': [
        {'name': 'id', 'type': 'int32'},
        {'name': 'nombre', 'type': 'string'},
        {'name': 'descripcion', 'type': 'string'},
        {'name': 'categoria_id', 'type': 'int32'},
        {'name': 'precio', 'type': 'float'},
        {'name': 'stock', 'type': 'int32'}
    ],
    'default_sorting_field': 'precio'
}

# Crear el índice en Typesense
try:
    client.collections['productos'].delete()
except Exception:
    pass

client.collections.create(schema)

# Poblar Typesense con datos de la base de datos
engine = get_engine()
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

productos = db.query(Producto).all()
for producto in productos:
    document = {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'categoria_id': producto.categoria_id,
        'precio': producto.precio,
        'stock': producto.stock
    }
    client.collections['productos'].documents.create(document)

db.close()

print("Datos sincronizados con Typesense.")
