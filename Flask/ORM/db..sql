 --Data base users, addresses and cars

CREATE SCHEMA IF NOT EXISTS orm_schema;

CREATE TABLE IF NOT EXISTS orm_schema.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS orm_schema.addresses (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES orm_schema.users (id)
);

CREATE TABLE IF NOT EXISTS orm_schema.cars (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES orm_schema.users (id)
);
