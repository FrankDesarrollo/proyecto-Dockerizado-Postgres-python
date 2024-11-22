GRANT SELECT ON ALL TABLES IN SCHEMA public TO replicator;
CREATE TABLE vehiculos (
    id SERIAL PRIMARY KEY,         -- Identificador único
    carro VARCHAR(100) NOT NULL,   -- Marca del carro
    color VARCHAR(50) NOT NULL,    -- Color del carro
    placa VARCHAR(10) NOT NULL     -- Placa del carro
);
