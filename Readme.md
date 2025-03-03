# **Documentación del Proyecto**

## **1. Introducción**
Este proyecto implementa un sistema de búsqueda rápida de entidades utilizando **Typesense** como VectorDB y una base de datos en **PostgreSQL** (hosteada en Supabase). La API ha sido desarrollada en **FastAPI**, con un esquema de base de datos en **SQLAlchemy**, contenedores Docker para la infraestructura y pruebas unitarias con **Pytest**.

## **2. Arquitectura del Proyecto**
### **Componentes Principales:**
- **Base de datos relacional (PostgreSQL)**: Contiene el modelo de datos estructurado con esquema en estrella.
- **VectorDB (Typesense)**: Maneja búsquedas eficientes sobre los productos.
- **API REST (FastAPI)**: Exposición de endpoints para CRUD y búsqueda.
- **Docker & Docker Compose**: Orquestación de servicios para ejecución local.
- **Pruebas unitarias (Pytest)**: Validación de la API.

## **3. Modelo de Datos**
El esquema de la base de datos sigue un modelo en estrella con las siguientes tablas:

- **productos** (Entidad principal)
- **categorias** (Dimensión)
- **usuarios** (Dimensión)
- **ventas** (Hechos relacionados a productos y usuarios)

## **4. Instalación y Configuración**
### **Requisitos:**
- Docker y Docker Compose
- Python 3.9+
- PostgreSQL (si se ejecuta sin Docker)

### **Pasos para ejecutar el proyecto:**

   ```
1. Levantar los contenedores:
   ```sh
   docker-compose up -d
   ```
2. Ejecutar migraciones de base de datos (si aplica):
   ```sh
   python database.py
   ```
3. Iniciar la API manualmente:
   ```sh
   uvicorn api_fastapi:app --reload --host 0.0.0.0 --port 8000
   ```

## **5. Endpoints de la API**

### **CRUD de Productos**
| Método  | Ruta              | Descripción                     |
|---------|------------------|---------------------------------|
| `POST`  | `/productos/`     | Crea un nuevo producto         |
| `GET`   | `/productos/`     | Lista todos los productos      |
| `GET`   | `/productos/{id}` | Obtiene un producto por ID     |
| `PUT`   | `/productos/{id}` | Actualiza un producto         |
| `DELETE`| `/productos/{id}` | Elimina un producto           |

### **Búsqueda en Typesense**
| Método  | Ruta              | Descripción                         |
|---------|------------------|-------------------------------------|
| `GET`   | `/search?q=text`  | Busca productos por nombre o desc. |

## **6. Pruebas Unitarias**
Para ejecutar las pruebas, correr:
```sh
pytest
```

