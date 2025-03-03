-- Creación de la base de datos (si no existe)
CREATE DATABASE datawarehouse;

-- Usar la base de datos
\c datawarehouse;

-- Tabla de Categorías
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Tabla de Productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    categoria_id INT REFERENCES categorias(id) ON DELETE SET NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

-- Tabla de Usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- Tabla de Ventas
CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES productos(id) ON DELETE CASCADE,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    cantidad INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para optimización de consultas
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_ventas_producto ON ventas(producto_id);
CREATE INDEX idx_ventas_usuario ON ventas(usuario_id);
