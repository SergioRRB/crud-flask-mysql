CREATE DATABASE bd_flask_python;
USE bd_flask_python;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL
);

DROP TABLE users;