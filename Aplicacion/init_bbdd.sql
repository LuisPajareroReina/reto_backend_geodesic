-- Archivo para crear una base de datos de prueba
-- NOTA: SI LA BASE DE DATOS TE DICE QUE NO TIENES PERMISOS REVISAR EL OWNER DE LAS TABLAS PSQL

-- Eliminar el contenido de las tablas o las tablas mismas si no existen previamente
DROP TABLE IF EXISTS Registro_acceso;
DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Acceso_perfil_punto;
DROP TABLE IF EXISTS Puntos;
DROP TABLE IF EXISTS perfil_acceso;

CREATE TABLE Puntos (
    ID_punto SERIAL PRIMARY KEY,
    nombre_instalacion VARCHAR(100),
    descripcion VARCHAR(100)
);

CREATE TABLE Perfil_acceso (
    ID_perfil_acceso SERIAL PRIMARY KEY,
    descripcion VARCHAR(100)
);


CREATE TABLE Usuarios (
    ID_usuario SERIAL PRIMARY KEY,
    ID_perfil_acceso INT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Empresa VARCHAR(50),
    password VARCHAR(50),
    FOREIGN KEY (ID_perfil_acceso) REFERENCES Perfil_acceso(ID_perfil_acceso)
);

CREATE TABLE Acceso_perfil_punto (
    ID_perfil_acceso INT,
    ID_punto INT,
	FOREIGN KEY (ID_perfil_acceso) REFERENCES Perfil_acceso(ID_perfil_acceso),
	FOREIGN KEY (ID_punto) REFERENCES Puntos(ID_punto)
);

CREATE TABLE Registro_acceso (
    ID_registro SERIAL PRIMARY KEY,
    ID_usuario INT,
    ID_punto INT,
    fecha_hora_acceso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_usuario) REFERENCES Usuarios(ID_usuario),
    FOREIGN KEY (ID_punto) REFERENCES Puntos(ID_punto)
);



INSERT INTO puntos (nombre_instalacion, descripcion) VALUES
--1
('GYM Talavera', 'Monitoreo de PH agua'),
('GYM Talavera', 'Monitoreo de tensión eléctrica punto 1'),
('GYM Talavera', 'Actuador Naranja'),
('GYM Talavera', 'Actuador Verde'),
--5
('GYM Valladolid', 'Monitoreo de PH agua'),
('GYM Valladolid', 'Actuador Azul'),
('GYM Valladolid', 'Contador de litros de agua'),
--8
('Empresa alimentaria', 'Monitoreo de PH agua'),
('Empresa alimentaria', 'Monitoreo nivel de agua'),
('Empresa alimentaria', 'Válvula de vaciado'),
('Empresa alimentaria', 'Actuador Naranja'),
('Empresa alimentaria', 'Actuador Morado');



INSERT INTO perfil_acceso (descripcion) VALUES
('Monitoreo GYM Talavera'), --1
('Actuador Naranja GYM Talavera'), --2
('Actuadores GYM Talavera'), --3
('Admin GYM Talavera y Valladolid'), --4

('Monitoreo GYM Talavera y Valladolid'), --5
('Mantenimiento GYM Valladolid'), --6
('Admin GYM Valladolid'), --7

('Monitoreo del tanque agua la empresa alimentaria'), --8
('Trabajadores de la planta de la empresa alimentaria'), --9
('Mantenimiento del tanque de agua'), --10
('Admin empresa alimentaria'); --11





INSERT INTO acceso_perfil_punto (ID_perfil_acceso, id_punto) VALUES
(1,1),
(1,2),

(2,3),

(3,3),
(3,4),

-- Carlos Rodriguez
(4,1),
(4,2),
(4,3),
(4,4),
(4,5),
(4,6),
(4,7),

-- Belen
(5,1),
(5,2),
(5,5),
(5,7),


(6,5),
(6,6),

(7,5),
(7,6),
(7,7),

(8,8),
(8,9),
(8,10),

(9,9),

(10,8),
(10,11),
(10,12),

(11,8),
(11,9),
(11,10),
(11,11),
(11,12);


INSERT INTO Usuarios (ID_perfil_acceso, Nombre, Apellido, Empresa, password) VALUES
(1, 'Alberto', 'Villalba', 'GYM X', '123456789'), --1
(2, 'Juan', 'Aprendiz', 'GYM X', '123456789'), --2
(3, 'Lucas', 'Veterano', 'GYM X', '123456789'),--3
(4, 'Carlos', 'Rodriguez', 'GYM X', 'admin'),--4
(2, 'Lucia', 'Aprendiz', 'GYM X', '123456789'),--5
(5, 'Belen', 'Sainz', 'GYM X', '123456789'),--6
(6, 'Pedro', 'Gomez', 'GYM X', '123456789'),--7
(6, 'Amancio', 'Sanchez', 'GYM X', '123456789'),
(7, 'Maria', 'Martin', 'GYM X', 'admin'),
(8, 'Javier', 'Morales', 'Empresa alimentaria', '123456789'),
(9, 'Lucia', 'Lopez', 'Empresa alimentaria', '123456789'),
(9, 'Mario', 'Sanz', 'Empresa alimentaria', '123456789'),
(9, 'Juan', 'Rubio', 'Empresa alimentaria', '123456789'),
(10, 'Paco', 'Jimenez', 'Empresa alimentaria', '123456789'),
(11, 'Fernando', 'Garcia', 'Empresa alimentaria', 'admin');

