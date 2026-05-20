CREATE TABLE clients
(
    code SERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    birth DATE,
    gender CHAR(1),
    address VARCHAR(200),
    house_number VARCHAR(20),
    telephone VARCHAR(20),
    email VARCHAR(150),
    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);