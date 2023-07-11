

-- Creación de la base de datos
CREATE DATABASE inventario_productos;

-- Seleccionar la base de datos
SELECT DATABASE() inventario_productos;

-- Creación de la tabla de productos             
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    descripcion TEXT,
    cantidad INT NOT NULL,
    precio_compra DECIMAL(10, 2) NOT NULL,
    precio_venta DECIMAL(10, 2) NOT NULL,
    proveedor_id INT NOT NULL REFERENCES proveedores(id),
    fecha_compra DATE NOT NULL,
    fecha_vencimiento DATE,
    ubicacion_id INT NOT NULL REFERENCES ubicaciones(id)
);

-- Creación de la tabla de movimientos de inventario
CREATE TABLE movimientos (
    id SERIAL PRIMARY KEY,
    producto_id INT NOT NUll REFERENCES productos(id),
    tipo_movimiento VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    fecha_movimiento DATE NOT NULL,
    usuario_responsable VARCHAR(100) NOT NULL,
    comentario TEXT
);

-- Creación de la tabla de proveedores
CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    correo_electronico VARCHAR(100),
    telefono VARCHAR(20),
    persona_contacto VARCHAR(100)
);

-- Creación de la tabla de ubicaciones
CREATE TABLE ubicaciones (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    descripcion TEXT,
    capacidad INT NOT NULL
);

-- Creación de la tabla de pedidos
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    numero_orden VARCHAR(20) NOT NULL,
    fecha_pedido DATE NOT NULL,
    proveedor_id INT NOT NULL REFERENCES proveedores(id),
    producto_id INT NOT NULL REFERENCES productos(id),
    cantidad INT NOT NULL,
    precio_compra DECIMAL(10, 2) NOT NULL,
    fecha_entrega_estimada DATE NOT NULL,
    fecha_entrega_real DATE
);

-- Creación de la tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    es_admin BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO productos (nombre, codigo, descripcion, cantidad, precio_compra, precio_venta, proveedor_id, fecha_compra, ubicacion_id)
VALUES 
    ('Detoditos', 'DT001', 'Snacks de maíz sabor a queso', 100, 1500, 2500, 1, '2023-05-08', 1),
    ('Margaritas', 'MG001', 'Snacks de maíz sabor a limón', 80, 1600, 2700,     2, '2023-05-08', 2),
    ('Doritos', 'DR001', 'Snacks de maíz sabor a chile', 120, 1500, 2600, 1, '2023-05-08', 3),
    ('Cheese', 'CH001', 'Snacks de queso', 90, 1400, 2500, 3, '2023-05-08', 1),
    ('Choclitos', 'CC001', 'Snacks de maíz sabor a chocolate', 70, 1200, 1900, 2, '2023-05-08', 2);


-- Agregar usuarios y administradores
INSERT INTO usuarios (nombre, email, password, es_admin) VALUES
    ('Usuario Normal', 'usuario@ejemplo.com', 'contraseña', FALSE),  
    ('Administrador', 'admin@ejemplo.com', 'contraseña', TRUE);

-- Asignar permisos de acceso
GRANT SELECT, INSERT, UPDATE, DELETE ON productos, movimientos, proveedores, ubicaciones, pedidos TO usuarios;
GRANT SELECT, INSERT, UPDATE, DELETE ON usuarios TO administrador; 









