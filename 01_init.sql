CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'replicator_password';
SELECT pg_create_physical_replication_slot('replication_slot');

CREATE TABLE pizza_orders (
    id SERIAL PRIMARY KEY,           -- Identificador único de cada pedido
    customer_name VARCHAR(100) NOT NULL,  -- Nombre del cliente
    pizza_type VARCHAR(50) NOT NULL,      -- Tipo de pizza pedida
    quantity INTEGER NOT NULL,            -- Cantidad de pizzas pedidas
    order_time TIMESTAMP DEFAULT NOW()    -- Fecha y hora del pedido
);

CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,         -- Identificador único
    carro VARCHAR(100) NOT NULL,   -- Marca del carro
    color VARCHAR(50) NOT NULL,    -- Color del carro
    placa VARCHAR(10) NOT NULL     -- Placa del carro
);
