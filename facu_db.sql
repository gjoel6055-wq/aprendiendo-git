CREATE DATABASE IF NOT EXISTS facultad;

CREATE TABLE IF NOT EXISTS alumnos (
    padron INT PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS materias (
    codido_materia INT  PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    carrera VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS notas (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo_materia INT NOT NULL,
    nota INT DEFAULT 0,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    padron INT NOT NULL,

    FOREIGN KEY (padron) REFERENCES alumnos(padron),
    FOREIGN KEY  (codigo_materia) REFERENCES  materias(codido_materia)
)
