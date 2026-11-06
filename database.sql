CREATE DATABASE IF NOT EXISTS usuarios_app;
USE usuarios_app;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (usuario, password) 
VALUES ('admin', '1234');

SELECT * FROM usuarios;

